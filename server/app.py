from flask import Flask, make_response, request
from loader import load_question_blueprints
from models import Question
from typing import Any, Dict

app = Flask(__name__)


@app.route("/question", methods=["POST", "GET"])
def question() -> Dict[str, Any]:
    user_answers_data = request.get_json()
    questions = load_question_blueprints()
    question = Question(
        questionId=questions[0]["questionId"],
        questionText=questions[0]["questionText"],
        questionFormat=questions[0]["questionFormat"],
        villagerTrait=questions[0]["villagerTrait"],
        answers=questions[0]["answers"][:4],
    )
    response = make_response(question)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
