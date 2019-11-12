from flask import Flask, render_templte
from urllib.request import urlopen
import json
app  = Flask(__name__)

@app.route("/")
def root():
  u = urllib.request.urlopen(
  "https://api.nasa.gov/planetary/apod?api_key=1qfeLB9B1j2icnEPSBgUipgKp2T2zi2SPvjXLYxQ"
  )
  response = u.read()
  data = json.loads(response)
  return render_template("index.html", pic = data['url'])

if __name__ == "__main__":
  app.debug = True
  app.run()
