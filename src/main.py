import yt_dlp as ydl

# Link to the YouTube video
link = "https://youtu.be/xC2ccYpjPHE?si=tBeqUUzvwp8-yaxG"

# Options for the download
ydl_opts = {
    'outtmpl': 'S:/coding/projects/Youtube video and Audio Downloader/YDownloader Python/videos/%(title)s.%(ext)s',  # Customize the path and filename
    'format': 'bestvideo+bestaudio/best',  # Download the best quality video and audio
}

try:
    with ydl.YoutubeDL(ydl_opts) as ydl_instance:
        ydl_instance.download([link])  # Downloads the video
    print('Video downloaded successfully!')
except Exception as e:
    print(f"Error during download: {e}")
