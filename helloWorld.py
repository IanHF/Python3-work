from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
	print(__name__) #where will this go?
	return "no hablo queso!"

@app.route("/college")
def wish():
    print(__name__)
    return "I really wish my college meetings weren't during softdev"


@app.route("/neck")
def complain():
    print(__name__)
    return "It's gonna be a pain in the neck keeping up with this class without attending in person"


@app.route("/static")
def narrate():
    print(__name__)
    file = open("occupations.csv", "r").read()
    return file

if __name__ == "__main__":
	app.debug = True
	app.run()