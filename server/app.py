import random

from flask import Flask, Response, request
from loader import load_question_blueprints, load_villagers
from models import Question, Villager, QuestionBlueprint
from typing import Any, Dict, Sequence

app = Flask(__name__)


@app.route("/question", methods=["POST", "GET"])
def question() -> Dict[str, Any]:
    user_answers_data = request.get_json()

    questions = load_question_blueprints()
    question = _generate_filter_question(questions)

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


def _generate_filter_question(
    questions: Sequence[QuestionBlueprint]
) -> Question:
    filter_question_ids = ["1", "2", "3", "4", "5"]
    # eventually we will also add "10", "11", "12", "13", "14", "15", "16", "17"

    random.shuffle(filter_question_ids)
    question_id = filter_question_ids[0]

    question_blueprint = _get_question_with_id(questions, question_id)

    random.shuffle(question_blueprint["answers"])

    return Question(
        questionId=question_blueprint["questionId"],
        questionText=question_blueprint["questionText"],
        questionFormat=question_blueprint["questionFormat"],
        villagerTrait=question_blueprint["villagerTrait"],
        answers=question_blueprint["answers"][:4],
    )


def _get_question_with_id(
    questions: Sequence[QuestionBlueprint],
    id: str
) -> QuestionBlueprint:
    for question in questions:
        if question["questionId"] == id:
            return question
