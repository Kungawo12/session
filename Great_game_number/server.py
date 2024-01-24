from flask import Flask,request, render_template, redirect, session
app = Flask(__name__)
import random

app.secret_key = 'Py Is Life'
@app.route('/')
def index():
    if "num" not in session:
        session["num"] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session["guess"]= int(request.form["guess"])
    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)