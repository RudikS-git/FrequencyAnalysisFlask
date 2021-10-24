from peewee import *

db = PostgresqlDatabase(
    'py_frequencyofwords',
    user='postgres',
    password='228058',
    host='localhost',
    port=5432
)


class BaseModel(Model):
    class Meta:
        database = db


class AnalysisResult(BaseModel):
    id = PrimaryKeyField(null=False)
    text_name = CharField(max_length=255)
    text = TextField()
    amount_numbers = BigIntegerField()
    amount_symbols = BigIntegerField()
    date_analysis = DateTimeField()

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'text_name': self.text_name,
            'text': self.text,
            'amount_numbers': self.amount_numbers,
            'amount_symbols': self.amount_symbols,
            'date_analysis': str(self.date_analysis),
        }

        return data

    # letters = models.ForeignKey(OneLetter, on_delete=models.CASCADE) #models.ManyToOneRel(to='one_letter', related_name='analysis_result', on_delete=models.CASCADE)

    class Meta:
        db_table = 'texts'


class OneLetter(BaseModel):
    id = PrimaryKeyField(null=False)
    content = CharField(max_length=1)
    amount = BigIntegerField()
    frequency = FloatField()
    analysis_result = ForeignKeyField(AnalysisResult, to_field="id", related_name="one_letters", on_delete='cascade')

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'content': self.content,
            'amount': self.amount,
            'frequency': self.frequency,
            'analysis_result_id': self.analysis_result,
        }

        return data

    class Meta:
        db_table = 'one_letters'


class TwoLetter(BaseModel):
    id = PrimaryKeyField(null=False)
    content = CharField(max_length=2)
    amount = BigIntegerField()
    frequency = FloatField()
    analysis_result = ForeignKeyField(AnalysisResult, to_field="id", related_name="two_letters", on_delete='cascade')

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'content': self.content,
            'amount': self.amount,
            'frequency': self.frequency,
            'analysis_result_id': self.analysis_result,
        }

        return data

    class Meta:
        db_table = 'two_letters'


class ThreeLetter(BaseModel):
    id = PrimaryKeyField(null=False)
    content = CharField(max_length=3)
    amount = BigIntegerField()
    frequency = FloatField()
    analysis_result = ForeignKeyField(AnalysisResult, to_field="id", related_name="three_letters", on_delete='cascade')

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'content': self.content,
            'amount': self.amount,
            'frequency': self.frequency,
            'analysis_result_id': self.analysis_result,
        }

        return data

    class Meta:
        db_table = 'three_letters'


class Word(BaseModel):
    id = PrimaryKeyField(null=False)
    content = CharField(max_length=255)
    amount = BigIntegerField()
    frequency = FloatField()
    analysis_result = ForeignKeyField(AnalysisResult, to_field="id", related_name="words", on_delete='cascade')

    @property
    def serialize(self):
        data = {
            'id': self.id,
            'content': self.content,
            'amount': self.amount,
            'frequency': self.frequency,
            'analysis_result_id': self.analysis_result,
        }

        return data

    class Meta:
        db_table = 'words'


def create_tables():
    AnalysisResult.create_table()
    OneLetter.create_table()
    TwoLetter.create_table()
    ThreeLetter.create_table()
    Word.create_table()


try:
    db.connect()
    create_tables()
except InternalError as px:
    print(str(px))
