# yt-dlp Flask Server

This Flask server downloads the best audio stream from a YouTube video using `yt-dlp` and returns it as a file.

## Endpoint

GET /download?id=VIDEO_ID

## Example

GET /download?id=dQw4w9WgXcQ

Returns: .m4a audio file of the video.

## Dependencies

- yt-dlp must be installed on the system (Render supports adding it in build script)