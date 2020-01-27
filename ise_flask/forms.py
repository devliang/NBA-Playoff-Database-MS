from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class SearchForm(FlaskForm):
		
	teamName = StringField('teamName')
	playerLastName = StringField('playerLastName')
	managerLastName = StringField('managerLastName')
	coachFirstName = StringField('coachFirstName')
	coachLastName = StringField('coachLastName')
	coachAge = IntegerField('coachAge')
	coachSalary = FloatField('coachSalary($million)')
	coachWorkingYears = IntegerField('coachWorkingYears')
	date = DateField('date')
	coachID = IntegerField('coachID')
	search = SubmitField('search')
	playerID = IntegerField('playerID')
	playerFirstName = StringField('playerFirstName')
	playerLastName = StringField('playerLastName')
	playerSuffix = StringField('playerSuffix')
	playerAge = IntegerField('playerAge')
	position = StringField('position')
	averagePoints = FloatField('averagePoints')
	averageMinutes = FloatField('averageMiniutes')
	gamePlay = IntegerField('gamePlay')
	gameID = IntegerField('gameID')
	teamCity = StringField('teamCity')
	winOrLose = StringField('winOrLose')
	finalScore = IntegerField('finalScore')
	refID = IntegerField('refID')
	venue = StringField('venue')
	initial = StringField('initial')
	division = StringField('division')
	champion = IntegerField('champion')
	totallySalary = FloatField('totallySalary($million)')
	managerID = IntegerField('managerID')
	conference = StringField('conference')
	refID = IntegerField('Referee ID')
	refFirstName = StringField('Referee First Name')
	refLastName = StringField('Referee Last Name')
	refID = IntegerField('Referee ID')
	age = StringField('Age')
	salary = FloatField('Salary')
	workingYears = IntegerField('Working Years')
	managerFirstName = StringField('managerFirstName')
	managerLastName = StringField('managerLastName')
	workingYears = IntegerField('workingYears')
	select = SelectField('sortBy', 
		choices=[('AGE','age'),('POS','position'),('AvgMin','average miniutes'),('GP','game play'),('AvgPoints','average points')])
	order = SelectField('orderBy',
		choices=[('DESC','descending'),('ASC','ascending')])
	winOrLose = SelectField('winOrLose',
		choices=[('W','win'),('L','lose')])







	


