from flask import Flask,render_template,redirect,request,session
app = Flask(__name__)
app.secret_key = "Py Is Life."
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/proceed', methods=['POST'])
def proceed():
    session["name"] = request.form['name']
    session["location"] = request.form['location']
    session["language"] = request.form['language']
    session["comment"] = request.form['comment']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('result.html')

@app.route('/home')
def home():
    session.clear()
    return redirect('/')
if __name__ == "__main__":
    app.run(debug=True,port=5001)