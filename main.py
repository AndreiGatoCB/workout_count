import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "68"
HEIGHT_CM = "165"
AGE = "30"

APP_ID = "app id"
API_KEY = "api key"
BEARER = "bearer"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_url = "https://api.sheety.co/09dfb348791902376d71e42b4111e88b/copiaDeMyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

today = datetime.now()

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

request_body = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(
    url=nutritionix_endpoint,
    json=request_body,
    headers=headers
)

result = response.json()
print(result)

time = today.strftime("%X")
date = today.strftime("%d/%m/%Y")

sheety_headers = {
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(
        url=sheety_url,
        json=sheet_inputs,
        headers=sheety_headers
    )

    print(sheet_response.text)
