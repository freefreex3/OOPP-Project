from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/home.html/')
def home():
    return render_template('home.html')

@app.route('/Repair.html/')
def Repair():
    return render_template('Repair.html')

@app.route('/Storage.html/')
def Storage():
    return render_template('Storage.html')

@app.route('/Profile.html/')
def Profile():
    return render_template('Profile.html')

if __name__ == "__main__":
    app.run(debug=True)

