
from flask import Flask, render_template,request, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configured database :;-
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



with app.app_context():
    db.create_all()

#

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":
        email = request.form["email"]
        password = request.form["password"]
        student=student.query.filter_by(email=email).first()

        if student:
            #check password
            if student.password == password:
                return render_template("/Student_dashboard")
            else:
                return "Incorrect password"
 
    return render_template("login.html")


@app.route("/register",methods=["GET","POST"])
def register():
    if request.method =="POST":
        name = request.form["name"]
        email = request.form["email"]
        password= request.form["password"]
         
        student = student(
            name = name,
            email = email,
            password = password
        )
        db.session.add(student)
        db.session.commit()

        print("Register button clicked!")
    return render_template("register.html")



@app.route("/student_dashboard")
def student_dashboard():
    return render_template("student_dashboard.html")

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")
@app.route("/feedback")
def feedback():
    return render_template("feedback.html")
@app.route("/student_dashboard")
def feedback_history():
    return render_template("feedback_history.html")
@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/reports")
def reports():
    return render_template("reports.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/setting")
def setting():
    return render_template("setting.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404

if __name__ == "__main__":

    app.run(debug=True)