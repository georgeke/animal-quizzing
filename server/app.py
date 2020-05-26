import os

from flask import Flask, Response, request, send_file
from loader import load_question_blueprints, load_villagers, load_answered_questions
from models import Question, Villager, QuestionBlueprint, AnsweredQuestion
from question_generator import generate_filter_question, generate_score_question
from typing import Any, Dict, Sequence

app = Flask(__name__)


SONGS_DIR = "db/songs"
NUM_FILTERED_QUESTIONS = 5
NUM_TOTAL_QUESTIONS = 10


@app.route("/question", methods=["POST", "GET"])
def question() -> Dict[str, Any]:
    user_answers_data = request.get_json()
    current_answers = load_answered_questions(user_answers_data["answers"])

    questions = load_question_blueprints()

    if len(current_answers) < NUM_FILTERED_QUESTIONS:
        question = generate_filter_question(questions, current_answers)
    elif len(current_answers) < NUM_TOTAL_QUESTIONS:
        question = generate_score_question(questions, current_answers)
    else:
        return {}

    return {
        "answers": current_answers,
        "nextQuestion": question,
    }


@app.route("/song", methods=["GET"])
def song() -> Response:
    song = request.args.get("name")

    all_songs = [f.split(".mp3")[0] for f in os.listdir(SONGS_DIR)]
    if song not in all_songs:
        return Response("Invalid song name", status=400)

    return send_file(
        f"../{SONGS_DIR}/{song}.mp3",
        mimetype="audio/mpeg",
        as_attachment=True,
        attachment_filename=f"{song}.mp3",
    )


@app.after_request
def update_cors(response: Response):
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response
