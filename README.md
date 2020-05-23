# animal-quizzing

## Dev Setup
Instructions only for Python3 on Mac.

Backend: (Run all in root directory)
 - Setup Virtual Environment: `python3 -m venv venv`
 - Install all package dependancies: `pip install -r requirements.txt`
 - Set environment variable for the Flask server entrypoint: `export FLASK_APP=server/app.py`
 - Set environment variable for development (auto refresh and better stacktraces): `export FLASK_ENV=development`
 - Start the server on `http://127.0.0.1:5000/`: `flask run`
 
Frontend (Run in frontend directory):
 - Install [Node](https://nodejs.org/en/download/)
 - Install all package dependancies: `yarn`
 - Start server: `yarn start`

## Misc

All resources from:
 - https://docs.google.com/spreadsheets/d/13d_LAJPlxMa_DubPTuirkIV4DERBMXbrWQsmSh8ReK4
 - https://github.com/NooksBazaar/google-sheets-to-json
