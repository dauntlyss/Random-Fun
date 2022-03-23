import requests
from googleapiclient.discovery import build

BASE_URL="http://www.boredapi.com/api"
AVAILABLE_TYPES=["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"]
API_KEY = 'AIzaSyBMtqOKrUGkSTWxqeecCLN5ywVL7xkVbBE'
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_random_activity():
    response= requests.get(f"{BASE_URL}/activity/")
    return response.json()

def get_activity_by_type(type):
    if type in AVAILABLE_TYPES:
        response= requests.get(f"{BASE_URL}/activity?type={type}")
        return response.json()
    return None
    
def get_videos(q, max_results):
    request = youtube.search().list(
        part='snippet', 
        maxResults=max_results,
        q=q
    )

    response = request.execute()
    # print(response)
    # print('*********')
    # print(response['items'][0]['snippet']['title'])



