import yt_dlp

def avai_format(link):
    ydl_opts = {
        'outtmpl': 'video_downloads/%(title)s.%(ext)s',
        'quiet': False,  # Set to False to show information about formats
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(link, download=False)
        formats = info_dict['formats']
        
        for fmt in formats:
            # Handle video formats with resolution and quality
            quality = fmt.get('quality', 'N/A')
            resolution = fmt.get('height', 'N/A') if 'height' in fmt else 'N/A'
            
            # For audio formats, skip the resolution and show bitrate if available
            acodec = fmt.get('acodec')  # Safely get acodec (None if not present)
            if acodec and acodec != 'none':
                print(f"Format ID: - {fmt['format_id']}, Quality: {quality}, Audio Bitrate: {fmt.get('abr', 'N/A')}, Extension: {fmt['ext']}")
            else:
                print(f"Format ID: - {fmt['format_id']}, Quality: {quality}, Resolution: {resolution}, Extension: {fmt['ext']}")
