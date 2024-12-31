import yt_dlp as ydl
import Knowformat
# YouTube video link
# link = "https://youtu.be/xC2ccYpjPHE?si=tBeqUUzvwp8-yaxG"
link = input("Enter Link : ")

allformat = input("To know the format available press Y for no press any button : ")
if "y" == allformat.lower():
    Knowformat.avai_format(link)


# Ask user for their choice
print("Choose download option:")
print("1. Audio Only")
print("2. Video Only")
print("3. Best Quality Video and Audio")
print("4. Low Quality Video and Audio")
print("5. Cancel Download")

user_input = input("Enter your choice (1/2/3/4/5): ").strip()



# Define download options based on user input
if user_input == "1":
    ydl_opts = {
        'outtmpl': 'S:/coding/projects/Youtube video and Audio Downloader/YDownloader Python/videos/%(title)s.%(ext)s',
        'format': 'bestaudio/best',  # Downloads best audio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
elif user_input == "2":
    ydl_opts = {
        'outtmpl': 'S:/coding/projects/Youtube video and Audio Downloader/YDownloader Python/videos/%(title)s.%(ext)s',
        'format': 'bestvideo[ext=mp4]',  # Downloads best video-only
    }
elif user_input == "3":
    ydl_opts = {
        'outtmpl': 'S:/coding/projects/Youtube video and Audio Downloader/YDownloader Python/videos/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',  # Downloads best video + best audio and merges them
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Converts output to MP4 if needed
        }],
    }
elif user_input == "4":
    ydl_opts = {
        'outtmpl': 'S:/coding/projects/Youtube video and Audio Downloader/YDownloader Python/videos/%(title)s.%(ext)s',
        'format': 'worstvideo+worstaudio/worst',  # Downloads worst quality video and audio
    }
else:
    print("Download Canceled")
    exit(1)

# Attempt download
try:
    with ydl.YoutubeDL(ydl_opts) as ydl_instance:
        ydl_instance.download([link])
    print('✅ Download completed successfully!')
except Exception as e:
    print(f"❌ Error during download: {e}")


