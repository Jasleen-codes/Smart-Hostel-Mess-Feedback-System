
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":
        # adding later updates 
        print("Login button clicked!")

    return render_template("login.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method =="POST":
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