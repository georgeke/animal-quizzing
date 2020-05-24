from flask import Flask, Response, request
from loader import load_question_blueprints, load_villagers, load_answered_questions
from models import Question, Villager, QuestionBlueprint, AnsweredQuestion
from question_generator import generate_filter_question, generate_score_question
from typing import Any, Dict, Sequence

app = Flask(__name__)


@app.route("/question", methods=["POST", "GET"])
def question() -> Dict[str, Any]:
    user_answers_data = request.get_json()
    current_answers = load_answered_questions(user_answers_data["answers"])

    questions = load_question_blueprints()

    if len(current_answers) < 5:
        question = generate_filter_question(questions, current_answers)
    else:
        question = generate_score_question(questions, current_answers)

    return {
        "answers": current_answers,
        "nextQuestion": question,
    }


@app.after_request
def update_cors(response: Response):
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response
