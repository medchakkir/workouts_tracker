import os
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Environment variables
app_id = os.getenv("APP_ID")
api_key = os.getenv("API_KEY")
api_token = os.getenv("API_TOKEN")
sheet_endpoint = os.getenv("SHEET_ENDPOINT")

# Define API endpoints
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


def get_user_input(prompt):
    return input(prompt)


def process_data(datas):
    today = datetime.now()
    exercise = datas["name"].title()
    duration = datas["duration_min"]
    nf_calories = datas["nf_calories"]

    inputs = {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise,
        "duration": duration,
        "calories": nf_calories
    }
    return inputs


# Set headers for API requests
exercise_headers = {
    "x-app-id": app_id,
    "x-app-key": api_key
}

sheet_headers = {
    "Authorization": api_token
}

# Get user input for exercises
exercise_text = get_user_input("Tell me which exercises you did: ")

# Send exercise data to Nutritionix API
response = requests.post(url=exercise_endpoint, json={"query": exercise_text}, headers=exercise_headers)
exercises = response.json()["exercises"]

# Process and log exercise data
for data in exercises:
    workout = process_data(data)
    sheet_inputs = {"workout": workout}
    print(sheet_inputs)

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=sheet_headers)
    print(sheet_response.status_code)
