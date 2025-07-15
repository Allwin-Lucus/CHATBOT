from flask import Flask, request, jsonify, send_from_directory
import aiml
import os

app = Flask(__name__, static_folder='.', static_url_path='')

bot = aiml.Kernel()

# Load brain or AIML
if os.path.exists("bot_brain.brn"):
    bot.bootstrap(brainFile="bot_brain.brn")
else:
    bot.bootstrap(learnFiles="startup.xml", commands="LOAD AIML B")
    bot.saveBrain("bot_brain.brn")

# Serve your HTML UI on /
@app.route("/")
def index():
    return send_from_directory('.', 'index.html')

# Serve other static files like CSS and JS
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

# API endpoint to receive message
@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get("message", "")
    bot_reply = bot.respond(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
  
    port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
