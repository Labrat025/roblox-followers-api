from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/followers/<int:user_id>', methods=['GET'])
def get_followers(user_id):
    url = f"https://users.roblox.com/v1/users/{user_id}/followers/count"
    
    try:
        # Anfrage an Roblox API
        response = requests.get(url)
        data = response.json()
        
        # Überprüfe, ob die Antwort gültig ist und die Follower-Zahl enthält
        if "count" in data:
            return jsonify({"user_id": user_id, "followers": data["count"]})
        else:
            return jsonify({"error": "User not found"}), 404
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Starte die Flask-App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
