#
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Smart Hostel Mess Feedback System"

if __name__ == "__main__":
    app.run(debug=True)