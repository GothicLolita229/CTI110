#CTI 110
#P5LAB5
#Lourdes Linares
#11.23.2021

from replit import web
import flask
import random

"""(double underscore, name, double underscore)"""
app = flask.Flask(__name__)

users = web.UserStore()

@app.route("/")
@web.authenticated
def index():
  name = "Strawberry"
  hits = users.current.get("hits", 0) + 1
  users.current["hits"] = hits

  #page = "This is " + name + "'s page"
  page = f"<p>This is 🍓{name}'s page</p>"
  page += f"<p>Hello, {web.auth.name}</p>"
  page += f"<p>You have been here {hits} times.</p>"
  page += """<a href = "/roll"> Roll a d6</a>"""

  return page

@app.route("/roll")
def rollDice():
  roll = random.randint(1,6)
  page = f"<h3>You rolled {roll} 🎲!</h3>"
  return page


# start progress
web.run(app)


#https://www.codewithrepl.it/static/code-with-replit.pdf