from flask import Flask, request, send_file, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/download', methods=['GET'])
def download_audio():
    video_id = request.args.get('id')
    if not video_id:
        return jsonify({"error": "Missing 'id' parameter"}), 400

    filename = f"{video_id}.m4a"
    filepath = os.path.join("/tmp", filename)
    url = f"https://www.youtube.com/watch?v={video_id}"

    try:
        subprocess.run([
            "yt-dlp", "-f", "bestaudio", "-x", "--audio-format", "m4a",
            "-o", filepath, url
        ], check=True)
        return send_file(filepath, as_attachment=True)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Download failed: {str(e)}"}), 500
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)