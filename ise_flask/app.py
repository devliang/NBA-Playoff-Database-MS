from flask import Flask, render_template, url_for, request
from forms import SearchForm
import mysql.connector


app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

def getNames():
	return ["JR", "RJ"]

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
	
	return render_template('home.html')

@app.route("/searchGame", methods=['GET', 'POST'])
def searchGame():
	form = SearchForm()
	if form.is_submitted():
		teamName = request.form['teamName']
		gameID = request.form['gameID']
		date = request.form['date']
		teamCity = request.form['teamCity']
		venue = request.form['venue']
		winOrLose = request.form['winOrLose']
		finalScore = request.form['finalScore']
		refID = request.form['refID']
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT * FROM Game WHERE TRUE "
			if teamName:
				query += "AND TEAMNAME = '" + teamName + "' "
			if gameID:
				query += "AND GameID = '" + gameID + "' "
			if date:
				query += "AND DATE = '" + date + "' "
			if teamCity:
				query += "AND TEAMCITY = '" + teamCity + "' "
			if venue:
				query += "AND VENUE = '" + venue + "' "
			if winOrLose:
				query += "AND WINorLOSE = '" + winOrLose + "' "
			if finalScore:
				query += "AND FinalScore = '" + finalScore + "' "
			if refID:
				query += "AND RefID = '" + refID + "' "
			print(query)
			mycursor.execute(query)

			myresult = mycursor.fetchall()
			titles = ["Game ID", "DATE", "Team City", "Team Name", "Venue", "WIN or LOSE", "Final Score", "Referee ID"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
	return render_template('searchGame.html', form=form)

@app.route("/searchPlayer", methods=['GET', 'POST'])
def searchPlayer():
	form = SearchForm()
	if form.is_submitted():
		teamName = str(request.form['teamName'])
		playerID = str(request.form['playerID'])
		playerFirstName = str(request.form['playerFirstName'])
		playerLastName = str(request.form['playerLastName'])
		playerSuffix = str(request.form['playerSuffix'])
		playerAge = str(request.form['playerAge'])
		position = str(request.form['position'])
		averageMinutes = str(request.form['averageMinutes'])
		gamePlay = str(request.form['gamePlay'])
		averagePoints = str(request.form['averagePoints'])
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT * FROM Player WHERE TRUE "
			if teamName:
				query += "AND TEAM = '" + teamName + "' "
			if playerID:
				query += "AND ID = '" + playerID + "' "
			if playerFirstName:
				query += "AND FirstName = '" + playerFirstName + "' "
			if playerLastName:
				query += "AND LastName = '" + playerLastName + "' "
			if playerSuffix:
				query += "AND SUFFIX = '" + playerSuffix + "' "
			if playerAge:
				query += "AND AGE = '" + playerAge + "' "
			if position:
				query += "AND POS = '" + position + "' "
			if averageMinutes:
				query += "AND AvgMin = '" + averageMinutes + "' "
			if gamePlay:
				query += "AND GP = '" + gamePlay + "' "
			if averagePoints:
				query += "AND AvgPoints = '" + averagePoints + "' "
			print(query)
			mycursor.execute(query)

			myresult = mycursor.fetchall()
			titles = ["ID", "First Name", "Last Name", "Suffix", "Position", "Age", "averageMinutes", "gamePlay", "averagePoints", "TEAM"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
			
	return render_template('searchPlayer.html', form=form)

@app.route("/searchTeam", methods=['GET', 'POST'])
def searchTeam():
	form = SearchForm()
	if form.is_submitted():
		teamName = request.form['teamName']
		teamCity = request.form['teamCity']
		initial = request.form['initial']
		conference = request.form['conference']
		division = request.form['division']
		champion = request.form['champion']
		totallySalary = request.form['totallySalary']
		managerID = request.form['managerID']
		coachID = request.form['coachID']
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT * FROM team WHERE TRUE "
			if teamCity:
				query += "AND TEAMCITY = '" + teamCity + "' "
			if teamName:
				query += "AND TEAMNAME = '" + teamName + "' "
			if coachID:
				query += "AND CoachID = '" + coachID + "' "
			if managerID:
				query += "AND ManagerID = '" + managerID + "' "
			if initial:
				query += "AND INITIALS = '" + initial + "' "
			if totallySalary:
				query += "AND totallySalary = '" + totallySalary + "' "
			if conference:
				query += "AND CONFERENCE = '" + conference + "' "
			if division:
				query += "AND DIVISION = '" + division + "' "
			if champion:
				query += "AND Champion = '" + champion + "' "
			print(query)
			mycursor.execute(query)
			myresult = mycursor.fetchall()
			titles = ["Team City", "Team Name", "Initials", "Conference", "Division", "Champion", "Totally Salary($million)", "ManagerID", "CoachID"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
	return render_template('searchTeam.html', form=form)

@app.route("/searchReferee", methods=['GET', 'POST'])
def searchReferee():
	form = SearchForm()
	if form.is_submitted():
		refID = request.form['refID']
		refFirstName = request.form['refFirstName']
		refLastName = request.form['refLastName']
		age = request.form['age']
		salary = request.form['salary']
		workingYears = request.form['workingYears']
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT * FROM Referee WHERE TRUE "
			if refID:
				query += "AND RefID = '" + refID + "' "
			if refFirstName:
				query += "AND FirstName = '" + refFirstName + "' "
			if refLastName:
				query += "AND LastName = '" + refLastName + "' "
			if age:
				query += "AND Age = '" + age + "' "
			if salary:
				query += "AND Salary = '" + salary + "' "
			if workingYears:
				query += "AND WorkingYears = '" + workingYears + "' "
			print(query)
			mycursor.execute(query)
			myresult = mycursor.fetchall()
			titles = ["RefereeID", "Referee First Name", "Referee Last Name", "Age", "Salary", "Working Years"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
	return render_template('searchReferee.html', form=form)

@app.route("/searchManager", methods=['GET', 'POST'])
def searchManager():
	form = SearchForm()
	if form.is_submitted():
		managerID = request.form['managerID']
		teamName = request.form['teamName']
		managerFirstName = request.form['managerFirstName']
		managerLastName = request.form['managerLastName']
		age = request.form['age']
		salary = request.form['salary']
		workingYears = request.form['workingYears']
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT * FROM Manager WHERE TRUE "
			if managerID:
				query += "AND ManagerID = '" + managerID + "' "
			if teamName:
				query += "AND TEAMNAME = '" + teamName + "' "
			if managerFirstName:
				query += "AND FirstName = '" + managerFirstName + "' "
			if managerLastName:
				query += "AND LastName = '" + managerLastName + "' "
			if age:
				query += "AND age = '" + age + "' "
			if salary:
				query += "AND Salary = '" + salary + "' "
			if workingYears:
				query += "AND WorkingYears = '" + workingYears + "' "
			print(query)
			mycursor.execute(query)
			myresult = mycursor.fetchall()
			titles = ["ManagerID", "Team Name", "First Name", "Last Name","Age", "Salary($million)", "Working Years"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
	return render_template('searchManager.html', form=form)

@app.route("/searchCoach", methods=['GET', 'POST'])
def searchCoach():
	form = SearchForm()
	if form.is_submitted():
		teamName = str(request.form['teamName'])
		coachID = str(request.form['coachID'])
		coachFirstName = str(request.form['coachFirstName'])
		coachLastName = str(request.form['coachLastName'])
		coachAge = str(request.form['coachAge'])
		coachSalary = str(request.form['coachSalary'])
		coachWorkingYears = str(request.form['coachWorkingYears'])
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT * FROM coach WHERE TRUE "
			if teamName:
				query += "AND TEAMNAME = '" + teamName + "' "
			if coachID:
				query += "AND CoachID = '" + coachID + "' "
			if coachFirstName:
				query += "AND FirstName = '" + coachFirstName + "' "
			if coachLastName:
				query += "AND LastName = '" + coachLastName + "' "
			if coachAge:
				query += "AND Age = '" + coachAge + "' "
			if coachSalary:
				query += "AND Salary = '" + coachSalary + "' "
			if coachWorkingYears:
				query += "AND WorkingYears = '" + coachWorkingYears + "' "
			print(query)
			mycursor.execute(query)

			myresult = mycursor.fetchall()
			titles = ["CoachID", "Team Name", "First Name", "Last Name", "Age", "Salary($million)", "Working Years"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
			
	return render_template('searchCoach.html', form=form)

@app.route("/searchQuery1", methods=['GET', 'POST'])
def query1():
	form = SearchForm()
	if form.is_submitted():
		teamName = str(request.form['teamName'])
		select = str(request.form['select'])
		order = str(request.form['order'])
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT * FROM player WHERE TRUE "
			if teamName:
				query += "AND TEAM = '" + teamName + "' "
			query += "ORDER BY " + select
			query += " " + order 
			print(query)
			mycursor.execute(query)

			myresult = mycursor.fetchall()
			titles = ["ID", "First Name", "Last Name", "Suffix", "Position", "Age", "averageMinutes", "gamePlay", "averagePoints", "TEAM"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
	return render_template('searchQuery1.html', form=form)

@app.route("/searchQuery2", methods=['GET', 'POST'])
def query2():
	form = SearchForm()
	if form.is_submitted():
		winOrLose = str(request.form['winOrLose'])
		order = str(request.form['order'])
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT team.TEAMCITY, team.TEAMNAME, game.WINorLOSE, game.FinalScore FROM team INNER JOIN (game INNER JOIN teamhasgame ON game.GameID = teamhasgame.GameID) ON team.TEAMNAME = teamhasgame.teamteam WHERE"
			query += " WINorLOSE = '" + winOrLose + "' "
			query += " ORDER BY FinalScore " + order
			print(query)
			mycursor.execute(query)
			myresult = mycursor.fetchall()
			titles = ["Tean City", "Team Name", "WIN or LOSE", "Final Score"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
	return render_template('searchQuery2.html', form=form)

@app.route("/searchQuery3", methods=['GET', 'POST'])
def query3():
	form = SearchForm()
	if form.is_submitted():
		winOrLose = str(request.form['winOrLose'])
		order = str(request.form['order'])
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT  Manager.FirstName, Manager.LastName, team.TEAMNAME,  COUNT(WINorLOSE) AS WonTimes\
				FROM Manager INNER JOIN (team INNER JOIN (game INNER JOIN teamhasgame ON game.GameID = teamhasgame.GameID)\
				ON team.TEAMNAME = teamhasgame.teamteam) ON manager.ManagerID = team.ManagerID\
				WHERE"
			query += " WINorLOSE = '" + winOrLose + "' "
			query += " GROUP BY Manager.FirstName, Manager.LastName, team.TEAMNAME"	
			query += " ORDER BY COUNT(WINorLOSE) " + order
			print(query)
			mycursor.execute(query)

			myresult = mycursor.fetchall()
			titles = ["First Name", "Last Name", "Team Name", "Times"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
	return render_template('searchQuery3.html', form=form)

@app.route("/searchQuery4", methods=['GET', 'POST'])
def query4():
	form = SearchForm()
	if form.is_submitted():
		winOrLose = str(request.form['winOrLose'])
		order = str(request.form['order'])
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			# query = "SELECT COUNT(referee.RefID) AS RefTimes,  game.WINorLOSE, referee.FirstName, referee.LastName, referee.WorkingYears\
			# 		FROM game INNER JOIN referee ON referee.RefID = game.RefID\
			# 		WHERE "

			query = "SELECT TEAMCITY, TEAMNAME, WINorLOSE, referee.RefID, FirstName, LastName, WorkingYears, COUNT(referee.RefID) AS RefTimes\
					FROM game INNER JOIN referee ON referee.RefID = game.RefID\
					WHERE "

			query += " WINorLOSE = '" + winOrLose + "' "
			query += " GROUP BY TEAMNAME"	
			query += " ORDER BY COUNT(referee.RefID) " + order
			print(query)
			mycursor.execute(query)

			myresult = mycursor.fetchall()
			# titles = ["RefTimes", "WIN or LOSE", "First Name", "Last Name", "WorkingYears"]
			titles = ["Team City", "Team Name", "WinOrLose", "RefID", "Ref First Name", "Ref Last Name", "Working Years", "Team Won Games With This Ref"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
	return render_template('searchQuery4.html', form=form)

@app.route("/searchQuery5", methods=['GET', 'POST'])
def query5():
	form = SearchForm()
	if form.is_submitted():
		#teamName = str(request.form['teamName'])
		order = str(request.form['order'])
		mydb = mysql.connector.connect(
	  	host="localhost",
	  	user="root",
	  	passwd="123456",
	  	database="NBA"
		)
		mycursor = mydb.cursor()
		if mycursor:
			query = "SELECT Player.FirstName, Player.LastName, ((Player.AvgPoints/Player.AvgMin)*Player.GP) AS MVPFactor\
					FROM Player\
					WHERE Player.AvgPoints <> 0 "
			#if teamName:
			#	query += "AND TEAM = '" + teamName + "' "
			query += " GROUP BY FirstName, LastName, MVPFactor"
			print(query)
			mycursor.execute(query)

			myresult = mycursor.fetchall()
			titles = ["First Name", "Last Name", "MVP Factor (Potential)"]
			return render_template('home.html', form=form, myresult=myresult, titles=titles)
	return render_template('searchQuery5.html', form=form)

if __name__ == '__main__':
	app.run(debug=True)