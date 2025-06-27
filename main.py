from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hack the planet'

@app.route('/index')
def death_code():
  return 'this is pascal'

if __name__ == '__main__':
  app.run(debug=True)