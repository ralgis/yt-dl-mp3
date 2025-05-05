# yt-dlp Flask Server (with embedded yt-dlp.py)

This Flask server downloads audio from YouTube using a locally bundled yt-dlp.py script.

## Endpoint

GET /download?id=VIDEO_ID

Returns: .m4a audio file.

## No external packages required beyond 'flask'.