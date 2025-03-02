from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/followers/<int:user_id>', methods=['GET'])
def get_followers(user_id):
    # Roblox API-URL für das Abrufen der Follower-Zahl
    url = f"https://users.roblox.com/v1/users/{user_id}/followers/count"
    
    try:
        # Anfrage an die Roblox API, um die Anzahl der Follower zu bekommen
        response = requests.get(url)
        
        # Überprüfen, ob die Antwort von Roblox korrekt ist
        if response.status_code == 200:
            data = response.json()
            
            # Überprüfen, ob das Feld "count" in den Daten vorhanden ist
            if "count" in data:
                return jsonify({
                    "user_id": user_id,
                    "followers": data["count"]
                })
            else:
                return jsonify({"error": "Follower count not found"}), 404
        else:
            return jsonify({"error": "Failed to retrieve data from Roblox"}), 500
    
    except Exception as e:
        # Fehlerbehandlung, falls etwas schiefgeht
        return jsonify({"error": str(e)}), 500

# Starte die Flask-Anwendung
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


@app.route('/')
def home():
    return "API is working! Go to /followers/<user_id> to check the follower count."


@app.route('/')
def home():
    return "API is working! Go to /followers/<user_id> to check the follower count."

