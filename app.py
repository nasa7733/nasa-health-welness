from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

RESOURCE_LIBRARY = [
    {
        "title": "Guided Breathing",
        "description": "A simple 4-7-8 breathing exercise to reduce stress.",
        "link": "https://www.healthline.com/health/4-7-8-breathing"
    },
    {
        "title": "Mindfulness Practice",
        "description": "Short guided mindfulness sessions for daily focus.",
        "link": "https://www.mindful.org/what-is-mindfulness/"
    },
    {
        "title": "Sleep Hygiene",
        "description": "Tips to improve sleep and restore energy.",
        "link": "https://www.sleepfoundation.org/sleep-hygiene"
    }
]

MOOD_RECOMMENDATIONS = {
    "sad": "Try a short walk, journaling, or calling a friend. If the feeling persists, reach out to a mental health professional.",
    "anxious": "Practice deep breathing and ground yourself with your senses. Small breaks can help lower stress.",
    "stressed": "Take a 5-minute break to stretch and breathe. Review your tasks and prioritize self-care.",
    "happy": "Celebrate your feelings and keep doing what supports your well-being.",
    "neutral": "A balanced routine of movement, rest, and connection can help maintain your mood."
}

BREATHING_EXERCISE = {
    "title": "4-7-8 Calming Breath",
    "steps": [
        "Breathe in quietly through your nose for 4 seconds.",
        "Hold your breath for 7 seconds.",
        "Exhale completely through your mouth for 8 seconds.",
        "Repeat for 4 rounds while focusing on the breath."
    ],
    "tip": "Use this when you feel anxious, stressed, or overwhelmed."
}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/resources", methods=["GET"])
def resources():
    return render_template("resources.html", resources=RESOURCE_LIBRARY)

@app.route("/breathing-exercise", methods=["GET"])
def breathing_exercise():
    return render_template("breathing.html", exercise=BREATHING_EXERCISE)

@app.route("/mood-check", methods=["GET", "POST"])
def mood_check():
    if request.method == "POST" and request.form:
        mood = request.form.get("mood", "neutral").strip().lower()
        notes = request.form.get("notes", "")
        recommendation = MOOD_RECOMMENDATIONS.get(mood, MOOD_RECOMMENDATIONS["neutral"])
        return render_template(
            "mood_check.html",
            mood=mood,
            notes=notes,
            recommendation=recommendation,
            resource=RESOURCE_LIBRARY[0]
        )

    return render_template("mood_form.html")

@app.route("/api/resources", methods=["GET"])
def api_resources():
    return jsonify({"resources": RESOURCE_LIBRARY})

@app.route("/api/breathing-exercise", methods=["GET"])
def api_breathing_exercise():
    return jsonify(BREATHING_EXERCISE)

@app.route("/api/mood-check", methods=["POST"])
def api_mood_check():
    data = request.get_json(silent=True) or {}
    mood = data.get("mood", "neutral").strip().lower()
    notes = data.get("notes", "")
    recommendation = MOOD_RECOMMENDATIONS.get(mood, MOOD_RECOMMENDATIONS["neutral"])

    return jsonify({
        "mood": mood,
        "notes": notes,
        "recommendation": recommendation,
        "resource": RESOURCE_LIBRARY[0]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
