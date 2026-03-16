from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def get_activities():
    response = client.get("/activities")
    return response

def signup_for_activity(activity_name, email):
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    return response

def unregister_participant(activity_name, email):
    response = client.delete(f"/activities/{activity_name}/unregister", params={"email": email})
    return response
