from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

# -------------------------------
# Flask App Configuration
# -------------------------------
app = Flask(__name__)

app.config["SECRET_KEY"] = "messvision_secret_2026"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# -------------------------------
# Database Models
# -------------------------------

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    meal = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)


# -------------------------------
# Home Page
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")

# -------------------------------
# Student Registration
# -------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if email already exists
        existing_student = Student.query.filter_by(email=email).first()

        if existing_student:
            flash("Email already exists. Please login.", "warning")
            return redirect(url_for("register"))

        # Create new student
        new_student = Student(
            name=name,
            email=email,
            password=password
        )

        db.session.add(new_student)
        db.session.commit()

        flash("Registration Successful! Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


# -------------------------------
# Student Login
# -------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        # Find student by email
        student = Student.query.filter_by(email=email).first()

        # Check email and password
        if student and student.password == password:

            # Store student details in session
            session["student_id"] = student.id
            session["student_name"] = student.name

            flash("Login Successful!", "success")

            # Redirect to Student Dashboard
            return redirect(url_for("student_dashboard"))

        elif student:
            flash("Incorrect password.", "danger")

        else:
            flash("Email not registered.", "danger")

    return render_template("login.html")


# -------------------------------
# Logout
# -------------------------------

@app.route("/logout")
def logout():

    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for("login"))


# -------------------------------
# Student Dashboard
# -------------------------------

@app.route("/student_dashboard")
def student_dashboard():
    if "student_id" not in session:
        flash("Please login first.", "warning")
        return redirect(url_for("login"))

    return render_template(
        "student_dashboard.html",
        student_name=session["student_name"]
    )

# -------------------------------
# Admin Dashboard
# -------------------------------

@app.route("/admin_dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")


# -------------------------------
# Feedback
# -------------------------------

@app.route("/feedback", methods=["GET", "POST"])
def feedback():

    if request.method == "POST":

        meal = request.form["meal"]
        rating = int(request.form["rating"])
        comment = request.form["comment"]

        new_feedback = Feedback(
            meal=meal,
            rating=rating,
            comment=comment
        )

        db.session.add(new_feedback)
        db.session.commit()

        flash("Feedback submitted successfully!", "success")
        return redirect(url_for("feedback"))

    return render_template("feedback.html")


# -------------------------------
# Other Pages
# -------------------------------

@app.route("/feedback_history")
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


# -------------------------------
# Error Page
# -------------------------------

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


# -------------------------------
# Create Database
# -------------------------------

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)