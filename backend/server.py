
import os
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0",
})

@app.route("/api/tracks")
def get_tracks():
    # TODO: Replace with your Instagram scraping logic
    return jsonify([
        {
            "id": "1",
            "title": "Sample Track",
            "audio_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        }
    ])

@app.route("/api/proxy")
def proxy():
    url = request.args.get("url")
    r = session.get(url, stream=True)
    return Response(r.iter_content(chunk_size=1024),
                    content_type=r.headers.get('content-type'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False, threaded=True)
