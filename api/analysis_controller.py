from datetime import datetime

from flask import jsonify, request, make_response
from flask_restful import Resource
from peewee import DoesNotExist
from playhouse.shortcuts import model_to_dict
from api.models import AnalysisResult, OneLetter, Word, ThreeLetter, TwoLetter
from businesslogic.analysis import Analysis
from businesslogic.filer_helper import FileHelper
from businesslogic.frequency.frequency_calculate import FrequencyCalculate
from businesslogic.letter_finder_way.letter_finder import LetterFinder
from businesslogic.numbersFinder.numbers_counter import NumbersCounter
from api.result import Result
from businesslogic.wordFinder.word_finder import WordFinder

class FileController(Resource):

    def get(self, id):

        analysis_controller = AnalysisController()
        data = str(analysis_controller.get(id))

        # no sense
        file_helper = FileHelper('./uploads')

        if(file_helper.create_directory()):
            file_helper.create_put_file('%s.txt' % str(id), data)
        #

        response = make_response(data)
        response.headers.set('Content-Type', 'text/plain')
        response.headers.set('Content-Disposition', 'attachment', filename='%s.txt' % str(id))

        return response


class AnalyzeController(Resource):

    def post(self):
        try:
            text = request.form['inputText']
            analysis = Analysis(text)

            letters = analysis.get_letter(LetterFinder())
            two_letters = analysis.get_two_letter(LetterFinder())
            three_letters = analysis.get_three_letter(LetterFinder())
            words = analysis.get_words(WordFinder())

            frequency_calculate = FrequencyCalculate()

            analysis_result = Result(
                analysis.get_frequence(frequency_calculate, letters, sum(item[1] for item in letters)),
                analysis.get_frequence(frequency_calculate, two_letters, sum(item[1] for item in two_letters)),
                analysis.get_frequence(frequency_calculate, three_letters, sum(item[1] for item in three_letters)),
                analysis.get_frequence(frequency_calculate, words, sum(item[1] for item in words)),
                analysis.get_numbers(NumbersCounter()),
                text
            )
        except ValueError as e:
            return jsonify(errorMessage=e)

        return jsonify(analysis_result.serialize())


class AnalysisListController(Resource):
    def get(self, page=1):
        per_page = 10
        analysisResults = (AnalysisResult
                           .select()
                           # .paginate(page, per_page) \
                           )

        data = [i.serialize for i in analysisResults]
        return data

    def post(self):
        json = request.get_json()

        # analysisResult = AnalysisResult()
        # analysisResult.amount_numbers = json['amount_numbers']
        # analysisResult.amount_symbols = json['amount_symbols']
        # analysisResult.text = json['text']
        # analysisResult.text_name = json['text_name']
        # analysisResult.date_analysis = datetime.now()
        # result = analysisResult.save()

        result = (AnalysisResult.insert(
            {
                'amount_numbers': json['amount_numbers'],
                'amount_symbols': json['amount_symbols'],
                'text': json['text'],
                'text_name': json['text_name'],
                'date_analysis': datetime.now()
            }
        )
                  .execute())

        (OneLetter.insert_many(
            [{'content': i['content'], 'amount': i['amount'], 'frequency': i['frequency'], 'analysis_result_id': result}
             for i in json['one_letters']]
        )
         .execute())

        (TwoLetter.insert_many(
            [{'content': i['content'], 'amount': i['amount'], 'frequency': i['frequency'], 'analysis_result_id': result}
             for i in json['two_letters']]
        )
         .execute())

        (ThreeLetter.insert_many(
            [{'content': i['content'], 'amount': i['amount'], 'frequency': i['frequency'], 'analysis_result_id': result}
             for i in json['three_letters']]
        )
         .execute())

        (Word.insert_many(
            [{'content': i['content'], 'amount': i['amount'], 'frequency': i['frequency'], 'analysis_result_id': result}
             for i in json['words']]
        )
         .execute())

        return True


class AnalysisController(Resource):
    def get(self, id, page=1):

        try:
            analysisResult = (AnalysisResult.get_by_id(id))
        except DoesNotExist:
            return jsonify(errorMessage='Object for this id does not exist')

        analysisResult.date_analysis = str(analysisResult.date_analysis)

        # oneLetters = [i.serialize for i in OneLetter.select().where(OneLetter.id == analysisResult.id)]
        # twoLetters = [i.serialize for i in TwoLetter.select().where(TwoLetter.id == analysisResult.id)]
        # threeLetters = [i.serialize for i in ThreeLetter.select().where(ThreeLetter.id == analysisResult.id)]
        # words = [i.serialize for i in Word.select().where(Word.id == analysisResult.id)]

        # .join(OneLetter, JOIN.LEFT_OUTER, on=(AnalysisResult.id == OneLetter.analysis_result))
        # .switch()
        # .join(TwoLetter, JOIN.LEFT_OUTER, on=(AnalysisResult.id == TwoLetter.analysis_result))
        # .join(ThreeLetter, on=(AnalysisResult.id == ThreeLetter.analysis_result))
        # .join(Word, on=(AnalysisResult.id == Word.analysis_result))

        return model_to_dict(analysisResult, backrefs=True)

    def delete(self, id):
        analysis_result = AnalysisResult.get(AnalysisResult.id == id)

        return analysis_result.delete_instance()
