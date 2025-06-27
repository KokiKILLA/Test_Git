from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hack the planet'

@app.route('/parity_check')
def parity_check():
  random_number = random.randrange(0, 9)
  if random_number % 2 == 0:
    return "чет"
  else:
    return "нечет"

@app.route('/index')
def death_code():
  return 'this is pascal'

app.route('/index_strange')
def pascal():
  return "very strange things"

if __name__ == '__main__':
  app.run(debug=True)