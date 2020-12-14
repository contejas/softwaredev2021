from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  names={"tejas":True, 
    "matthew":False, 
    "daniel":True, 
    "ben":True, 
    "jane":True, 
    "alex":False, 
    "jay": True}
  message = "Welcome to Software Dev!"
  return render_template('index.html', message=message, names=names)

@app.route('/')
def another():
  return """ Hidden Page """

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)