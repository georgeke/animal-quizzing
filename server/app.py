import random

from flask import Flask, Response, request
from loader import load_question_blueprints
from models import Question
from typing import Any, Dict

app = Flask(__name__)


@app.route("/question", methods=["POST", "GET"])
def question() -> Dict[str, Any]:
    user_answers_data = request.get_json()
    questions = load_question_blueprints()
    random.shuffle(questions[0]["answers"])
    question = Question(
        questionId=questions[0]["questionId"],
        questionText=questions[0]["questionText"],
        questionFormat=questions[0]["questionFormat"],
        villagerTrait=questions[0]["villagerTrait"],
        answers=questions[0]["answers"][:4],
    )
    return {
        "answers": user_answers_data["answers"],
        "nextQuestion": question,
    }

@app.after_request
def update_cors(response: Response):
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response
