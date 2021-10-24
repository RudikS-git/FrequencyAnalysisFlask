from flask import Flask, jsonify
from flask_restful import Resource, Api
from api.analysis_controller import AnalysisController, AnalyzeController, AnalysisListController, FileController
from api.models import AnalysisResult, OneLetter, TwoLetter, ThreeLetter, Word
from peewee import PostgresqlDatabase, Model

UPLOAD_FOLDER = 'uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

api = Api(app)

api.add_resource(AnalysisController, '/analysis/<id>')
api.add_resource(AnalysisListController, '/analysis')
api.add_resource(AnalyzeController, '/analyze')
api.add_resource(FileController, '/analysis-file/<id>')

if __name__ == '__main__':
    app.run()
