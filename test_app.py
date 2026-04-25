import json
from app import app

def test_home_ui_renders_html():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "Nasa's Health & Mental Wellness Hub" in html
    assert "Wellness Resources" in html or "Mood Check" in html

def test_api_resources_contains_library():
    client = app.test_client()
    response = client.get("/api/resources")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data["resources"], list)
    assert len(data["resources"]) >= 1

def test_api_breathing_exercise_endpoint():
    client = app.test_client()
    response = client.get("/api/breathing-exercise")
    assert response.status_code == 200
    data = response.get_json()
    assert "steps" in data
    assert len(data["steps"]) == 4

def test_api_mood_check_recommendation_for_anxious():
    client = app.test_client()
    payload = {"mood": "anxious", "notes": "Feeling nervous about a presentation."}
    response = client.post("/api/mood-check", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["mood"] == "anxious"
    assert "breathing" in data["recommendation"].lower() or "stress" in data["recommendation"].lower()


def test_diet_guidance_ui_renders_html():
    client = app.test_client()
    response = client.get("/diet-guidance")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "Diet Guidance" in html
    assert "Elder People" in html
