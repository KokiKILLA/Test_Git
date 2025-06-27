from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hack the planet'

app.route('/index')
def pascal():
  return "very strange things"

if __name__ == '__main__':
  app.run(debug=True)