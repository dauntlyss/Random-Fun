import requests

BASE_URL="http://www.boredapi.com/api"
AVAILABLE_TYPES=["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]

def get_random_activity():
    response= requests.get(f"{BASE_URL}/activity/")
    return response.json()

def get_activity_by_type(type):
    if type in AVAILABLE_TYPES:
        response= requests.get(f"{BASE_URL}/activity?type={type}")
        return response.json()
    return None

