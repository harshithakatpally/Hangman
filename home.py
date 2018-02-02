from bottle import route,run,Bottle,template,request

import random,pymsgbox

actorsl = ['Leonardo DiCaprio':'The actor was born on November 11, 1974', 'Rowan Atkinson':'His spouse is Sunetra Sastry', 'Tom Hanks':'One of the actor\'s child is Truman Theodore', 'Tom Cruise':'The actor has won three Golden Globe Awards', 'Dwayne Johnson':'The person is an actor and professional wrestler', 'Johnny Depp':'The actor has won 3 Academy Awards and the Golden Globe and Screen Actors Guild Award for Best Actor', 'Matt Damon':'The person is an American actor, film producer, philanthropist and Screenwriter','Brad Pitt':'He owns the Plan B Enternainment company']
singersl = ['Rihanna':'Anti is one of the singer\'s music albums', 'justin beaber':'The singer is the 10th-most followed singer on instagram', 'Taylor Swift':'The singer is known for narrative songs about her personal life', 'Katy Perry':'The actor started career in Gospel music as a teenager', 'Lady Gaga':'Full name of the actor is Stefani Joanne Angelina Germanotta', 'Selena Gomez':'The actor started career starring in the chldren\'s telivision series Barney&Friends']
sportsmenl = ['Michael Jordan':'The person is the principal owner and chairman of the Charlotte Hornets of the National Basketball Association', 'Usain Bolt':'The person is a retired Jamaican Sprinter','Michael Phelps':'The person went to the University of Michigan', 'Andy Murray':'The spouse is Kim Sears', 'Lewis Hamilton':'The person races in Formula One for Mercedes AMG Petronas team', 'Saina Nehwal':'The person is he former world no. 1 in badminton', 'P T Usha':'The person is often called Queen of Indian track and field', 'Ricky Ponting':'The person is a two world cup winning captain in 2003 and 2007']
moviesl = ['Justice League':'The director of this movie is Zack Snyder', 'Saving Private Ryan':'Tom Hanks is the leading role in this movie', 'Titanic':'The director of this movie is James Cameron', 'Harry Potter':'This movie is an adaptation of a famous hildren\'s novel', 'Fight Club':'The story of this movie was written by Chuck Palahniuk', 'Citizen Kane':'This movie was released on September 5, 1941', 'Die Hard':' Joel Silver, Lawrence Gordon are the producers of this movie', 'Avatar':'This movie is the fifth-fastest-grossing film worldwide by days to milestone']
countriesl = ['India':'The highest peak in the world is located in this country', 'United States':'This country had 50 states', 'China':'This country had the highest population in the world', 'Japan':'Tokyo is the capital of this country', 'Sri Lanka':'This is an island nation', 'Pakistan':'This is the fifth-most populous country', 'Russia':'It is the worl\'s largest nation']

vowels = ['a', 'e', 'i', 'o', 'u']

app=Bottle()
app.rands = None
app.score = 0
app.attempt = 0
app.randl = None
app.randstr = None
app.hint = None
app.guessedlist = None

@app.route('/')
def home():
	return template('hang')

@app.post('/check')
def check():
	flag = 0
	checkc = request.forms.get('alphabet')
	checkc = checkc.lower()
	if len(checkc) == 1:
		if checkc in app.guessedlist:
			flag = 1
			pymsgbox.alert('letter already entered', 'error')
		if checkc not in app.guessedlist:
			app.guessedlist.append(checkc)
			for j in range(len(app.rands)):
				if checkc == app.rands[j]:
					flag = 1
					app.randl[j] = checkc
	else:
		flag = 1
		pymsgbox.alert('Please enter a single letter', 'error')
	if checkc not in 'abcdefghijklmnopqrstuvwxyz':
		flag = 1
		pymsgbox.alert('please enter alphabets only', 'error')
	if flag == 0:
		pymsgbox.alert('Letter not in word')
		app.attempt = app.attempt - 1
		if(app.attempt == 0):
			del app.guessedlist[:]
			if(app.score > 0):
				app.score = app.score - 1
			return template('nextq', question = app.rands, score = app.score)
	rand = "".join(app.randl)
	randlist = list(app.rands)
	for i in range(len(app.rands)):
		if randlist[i] == ' ':
			randlist[i] = '|'
	if randlist == app.randl:
		app.score = app.score+1
		del app.guessedlist[:]
		return template('nextq', question = rand, score = app.score)
	return template('hangques', hint = app.hint, guessedlist = app.guessedlist, question = rand, score = app.score, attempt = app.attempt)


@app.route('/actors')
def actors():
	app.guessedlist = ['a','e','i','o','u']
	app.attempt = 10
	rand = random.choice(actorsl.keys())
	app.hint = actorsl[rand]
	app.rands = rand
	app.randl = list(rand)
	for i in range(len(rand)):
		if app.randl[i] not in vowels:
			if app.randl[i] == ' ':
				app.randl[i] = '|'
			else:
				app.randl[i] = " _ "
	rand = "".join(app.randl)
	return template('hangques', guessedlist = app.guessedlist, score = app.score, question = rand, attempt = app.attempt, hint = app.hint)

@app.route('/sportsmen')
def sportsmen():
	app.guessedlist = ['a','e','i','o','u']
	app.attempt = 10
	rand = random.choice(sportsmenl.keys())
	app.hint = actorsl[rand]
	app.rands = rand
	app.randl = list(rand)
	for i in range(len(rand)):
		if app.randl[i] not in vowels:
			if app.randl[i] == ' ':
				app.randl[i] = '|'
			else:
				app.randl[i] = " _ "
	rand = "".join(app.randl)
	return template('hangques', guessedlist = app.guessedlist, score = app.score, question = rand, attempt = app.attempt, hint = app.hint)

@app.route('/singers')
def singers():
	app.guessedlist = ['a','e','i','o','u']
	app.attempt = 10
	rand = random.choice(singersl.keys())
	app.hint = actorsl[rand]
	app.rands = rand
	app.randl = list(rand)
	for i in range(len(rand)):
		if app.randl[i] not in vowels:
			if app.randl[i] == ' ':
				app.randl[i] = '|'
			else:
				app.randl[i] = " _ "
	rand = "".join(app.randl)
	return template('hangques', guessedlist = app.guessedlist, score = app.score, question = rand, attempt = app.attempt, hint = app.hint)

@app.route('/movies')
def movies():
	app.guessedlist = ['a','e','i','o','u']
	app.attempt = 10
	rand = random.choice(moviesl.keys())
	app.hint = actorsl[rand]
	app.rands = rand
	app.randl = list(rand)
	for i in range(len(rand)):
		if app.randl[i] not in vowels:
			if app.randl[i] == ' ':
				app.randl[i] = '|'
			else:
				app.randl[i] = " _ "
	rand = "".join(app.randl)
	return template('hangques', guessedlist = app.guessedlist, score = app.score, question = rand, attempt = app.attempt, hint = app.hint)

@app.route('/countries')
def countries():
	app.guessedlist = ['a','e','i','o','u']
	app.attempt = 10
	rand = random.choice(countriesl.keys())
	app.hint = actorsl[rand]
	app.rands = rand
	app.randl = list(rand)
	for i in range(len(rand)):
		if app.randl[i] not in vowels:
			if app.randl[i] == ' ':
				app.randl[i] = '|'
			else:
				app.randl[i] = " _ "
	rand = "".join(app.randl)
	return template('hangques', guessedlist = app.guessedlist, score = app.score, question = rand, attempt = app.attempt, hint = app.hint)

run(app, host = 'localhost', port = 7777, debug = True)
