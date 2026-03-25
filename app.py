from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from agent import fitness_agent

app = Flask(__name__)
CORS(app)

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define model

class FitnessRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    weight = db.Column(db.Float)
    height = db.Column(db.Float)
    goal = db.Column(db.String(20))
    bmi = db.Column(db.Float)
    calories = db.Column(db.Integer)
    exercises = db.Column(db.String(255))
    tips = db.Column(db.String(255))

# ✅ Create tables immediately (Flask 3.x compatible)
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    age = data.get("age")
    weight = data.get("weight")
    height = data.get("height")
    goal = data.get("goal")

    recommendations = fitness_agent(age, weight, height, goal)

    # Save to DB
    record = FitnessRecord(
        age=age, weight=weight, height=height, goal=goal,
        bmi=recommendations['bmi'],
        calories=recommendations['calories'],
        exercises=", ".join(recommendations['exercises']),
        tips=" ".join(recommendations['tips'])
    )
    db.session.add(record)
    db.session.commit()

    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
