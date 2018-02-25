from bottle import route,run,Bottle,template,request

import random,pymsgbox

actorslist = ['Leonardo DiCaprio':'The actor was born on November 11, 1974', 'Rowan Atkinson':'His spouse is Sunetra Sastry', 'Tom Hanks':'One of the actor\'s child is Truman Theodore', 'Tom Cruise':'The actor has won three Golden Globe Awards', 'Dwayne Johnson':'The person is an actor and professional wrestler', 'Johnny Depp':'The actor has won 3 Academy Awards and the Golden Globe and Screen Actors Guild Award for Best Actor', 'Matt Damon':'The person is an American actor, film producer, philanthropist and Screenwriter','Brad Pitt':'He owns the Plan B Enternainment company']
singerslist = ['Rihanna':'Anti is one of the singer\'s music albums', 'justin beaber':'The singer is the 10th-most followed singer on instagram', 'Taylor Swift':'The singer is known for narrative songs about her personal life', 'Katy Perry':'The actor started career in Gospel music as a teenager', 'Lady Gaga':'Full name of the actor is Stefani Joanne Angelina Germanotta', 'Selena Gomez':'The actor started career starring in the chldren\'s telivision series Barney&Friends']
sportsmenlist = ['Michael Jordan':'The person is the principal owner and chairman of the Charlotte Hornets of the National Basketball Association', 'Usain Bolt':'The person is a retired Jamaican Sprinter','Michael Phelps':'The person went to the University of Michigan', 'Andy Murray':'The spouse is Kim Sears', 'Lewis Hamilton':'The person races in Formula One for Mercedes AMG Petronas team', 'Saina Nehwal':'The person is he former world no. 1 in badminton', 'P T Usha':'The person is often called Queen of Indian track and field', 'Ricky Ponting':'The person is a two world cup winning captain in 2003 and 2007']
movieslist = ['Justice League':'The director of this movie is Zack Snyder', 'Saving Private Ryan':'Tom Hanks is the leading role in this movie', 'Titanic':'The director of this movie is James Cameron', 'Harry Potter':'This movie is an adaptation of a famous hildren\'s novel', 'Fight Club':'The story of this movie was written by Chuck Palahniuk', 'Citizen Kane':'This movie was released on September 5, 1941', 'Die Hard':' Joel Silver, Lawrence Gordon are the producers of this movie', 'Avatar':'This movie is the fifth-fastest-grossing film worldwide by days to milestone']
countrieslist = ['India':'The highest peak in the world is located in this country', 'United States':'This country had 50 states', 'China':'This country had the highest population in the world', 'Japan':'Tokyo is the capital of this country', 'Sri Lanka':'This is an island nation', 'Pakistan':'This is the fifth-most populous country', 'Russia':'It is the worl\'s largest nation']

vowels = ['a', 'e', 'i', 'o', 'u']

app=Bottle()
app.wordstring = None
app.score = 0
app.attempts = 0
app.wordlist = None
app.hint = None
app.guessedlist = None

#Returns the categories.html page where categories are displayed
@app.route('/')
def home():
	return template('categories')

#Checks if the character entered is valid and is present in the word else performs necessary actions
@app.post('/check')
def check():
	flag = 0
	character = request.forms.get('alphabet')
	character = character.lower()
	if len(character) == 1:
		if character in app.guessedlist:
			flag = 1
			pymsgbox.alert('letter already entered', 'error')
		if character not in app.guessedlist:
			app.guessedlist.append(character)
			for j in range(len(app.wordstring)):
				if character == app.wordstring[j]:
					flag = 1
					app.wordlist[j] = character
	else:
		flag = 1
		pymsgbox.alert('Please enter a single letter', 'error')
	if character not in 'abcdefghijklmnopqrstuvwxyz':
		flag = 1
		pymsgbox.alert('please enter alphabets only', 'error')
	if flag == 0:
		pymsgbox.alert('Letter not in word')
		app.attempts = app.attempts - 1
		if(app.attempts == 0):
			del app.guessedlist[:]
			if(app.score > 0):
				app.score = app.score - 1
			return template('nextword', question = app.wordstring, score = app.score)
	randomword = "".join(app.wordlist)
	tempwordlist = list(app.wordstring)
	for i in range(len(app.wordstring)):
		if tempwordlist[i] == ' ':
			tempwordlist[i] = '|'
	if tempwordlist == app.wordlist:
		app.score = app.score+1
		del app.guessedlist[:]
		return template('nextword', question = randomword, score = app.score)
	return template('displayword', hint = app.hint, guessedlist = app.guessedlist, question = randomword, score = app.score, attempts = app.attempts)

#When actors category is selected, this function is called and returns displayword.html with words one after another
@app.route('/actors')
def actors():
	app.guessedlist = ['a','e','i','o','u']
	app.attempts = 10
	randomword = random.choice(actorslist.keys())
	app.hint = actorslist[randomword]
	app.wordstring = randonword
	app.wordlist = list(randonword)
	for i in range(len(randomword)):
		if app.wordlist[i] not in vowels:
			if app.wordlist[i] == ' ':
				app.wordlist[i] = '|'
			else:
				app.wordlist[i] = " _ "
	randomword = "".join(app.wordlist)
	return template('displayword', guessedlist = app.guessedlist, score = app.score, question = randomword, attempts = app.attempts, hint = app.hint)

#When singers category is selected, this function is called and returns displayword.html with words one after another
@app.route('/singers')
def singers():
	app.guessedlist = ['a','e','i','o','u']
	app.attempts = 10
	randomword = random.choice(singerslist.keys())
	app.hint = singerslist[randomword]
	app.wordstring = randomword
	app.wordlist = list(randomword)
	for i in range(len(randomword)):
		if app.wordlist[i] not in vowels:
			if app.wordlist[i] == ' ':
				app.wordlist[i] = '|'
			else:
				app.wordlist[i] = " _ "
	randomword = "".join(app.wordlist)
	return template('displayword', guessedlist = app.guessedlist, score = app.score, question = randomword, attempts = app.attempts, hint = app.hint)

#When sportsmen category is selected, this function is called and returns displayword.html with words one after another
@app.route('/sportsmen')
def sportsmen():
	app.guessedlist = ['a','e','i','o','u']
	app.attempts = 10
	randomword = random.choice(sportsmenlist.keys())
	app.hint = sportsmenlist[randomword]
	app.wordstring = randomword
	app.wordlist = list(randomword)
	for i in range(len(randomword)):
		if app.wordlist[i] not in vowels:
			if app.wordlist[i] == ' ':
				app.wordlist[i] = '|'
			else:
				app.wordlist[i] = " _ "
	randomword = "".join(app.wordlist)
	return template('displayword', guessedlist = app.guessedlist, score = app.score, question = randomword, attempts = app.attempts, hint = app.hint)

#When movies category is selected, this function is called and returns displayword.html with words one after another
@app.route('/movies')
def movies():
	app.guessedlist = ['a','e','i','o','u']
	app.attempts = 10
	randomword = random.choice(movieslist.keys())
	app.hint = movieslist[rand]
	app.wordstring = randomword
	app.wordlist = list(randomword)
	for i in range(len(randomword)):
		if app.wordlist[i] not in vowels:
			if app.wordlist[i] == ' ':
				app.wordlist[i] = '|'
			else:
				app.wordlist[i] = " _ "
	randomword = "".join(app.wordlist)
	return template('displayword', guessedlist = app.guessedlist, score = app.score, question = randomword, attempts = app.attempts, hint = app.hint)

#When countries category is selected, this function is called and returns displayword.html with words one after another
@app.route('/countries')
def countries():
	app.guessedlist = ['a','e','i','o','u']
	app.attempts = 10
	randomword = random.choice(countrieslist.keys())
	app.hint = countrieslist[randomword]
	app.wordstring = randomword
	app.wordlist = list(randomword)
	for i in range(len(randomword)):
		if app.wordlist[i] not in vowels:
			if app.wordlist[i] == ' ':
				app.wordlist[i] = '|'
			else:
				app.wordlist[i] = " _ "
	randomword = "".join(app.wordlist)
	return template('displayword', guessedlist = app.guessedlist, score = app.score, question = randomword, attempts = app.attempts, hint = app.hint)

run(app, host = 'localhost', port = 7777, debug = True)
