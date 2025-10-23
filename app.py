from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

# Load rituals
with open("rituals.json") as f:
    rituals = json.load(f)

# Pre-made ritual questions pool
questions_pool = [
    {"question": "What is the first ritual of the day?", "options": ["Meditation", "Gratitude Journaling", "Workout", "Learning"], "answer": "Gratitude Journaling"},
    {"question": "How many key tasks should you plan each day?", "options": ["1", "2", "3", "5"], "answer": "3"},
    {"question": "What should you do at the end of the day?", "options": ["Reflect on 1 win & 1 lesson", "Sleep immediately", "Check phone", "Skip planning"], "answer": "Reflect on 1 win & 1 lesson"},
    {"question": "Which ritual boosts your energy in the morning?", "options": ["Quick workout", "Scrolling phone", "Watching TV", "Sleeping"], "answer": "Quick workout"},
    {"question": "Why is gratitude journaling important?", "options": ["Builds focus", "Wastes time", "Makes you lazy", "None"], "answer": "Builds focus"},
    {"question": "How long should a morning mindset ritual take?", "options": ["1 min", "5-10 mins", "1 hour", "Whole day"], "answer": "5-10 mins"},
    {"question": "Which ritual helps you track daily growth?", "options": ["Reflection", "Watching TV", "Gaming", "Skipping tasks"], "answer": "Reflection"},
    {"question": "When should you plan your 3 key tasks?", "options": ["Morning", "Night", "After lunch", "Before sleep"], "answer": "Morning"},
    {"question": "What is the main goal of the 100 Days Challenge?", "options": ["Consistency", "Random fun", "Sleep more", "Ignore tasks"], "answer": "Consistency"},
    {"question": "Which ritual keeps your mind sharp?", "options": ["Skill growth / learning", "Sleeping", "Scrolling social media", "Watching TV"], "answer": "Skill growth / learning"}
]

@app.route("/")
def index():
    day = random.choice(rituals)
    ritual = day["ritual"]
    quiz_questions = random.sample(questions_pool, 5)  # pick 5 random questions
    return render_template("index.html", ritual=ritual, questions=quiz_questions)

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    score = 0
    for q in data["questions"]:
        if q["selected"] == q["answer"]:
            score += 1
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(debug=True)

