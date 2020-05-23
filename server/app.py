from flask import Flask, request
from loader import load_questions
from typing import Any, Dict

app = Flask(__name__)


@app.route("/question", methods=["POST", "GET"])
def question() -> Dict[str, Any]:
    user_answers_data = request.get_json()
    questions = load_questions()
    questions[0]["answers"] = questions[0]["answers"][:4]
    return questions[0]
