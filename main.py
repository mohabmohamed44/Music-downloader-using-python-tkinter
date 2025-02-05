import os
import re
from yt_dlp import YoutubeDL
import tkinter as tk
from tkinter import simpledialog


def sanitize_filename(filename):
    """Removes invalid characters for file names."""
    return re.sub(r'[<>:"/\\|?*]', "", filename)


def download_youtube_audio(url, output_folder="downloads"):
    """
    Downloads a YouTube video as an MP3 file, saves the title, and thumbnail.

    :param url: YouTube video URL
    :param output_folder: Folder to save the files (default: 'downloads')
    """
    try:
        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Configure yt-dlp options
        ydl_opts = {
            "format": "bestaudio/best",  # Download the best quality audio
            "outtmpl": os.path.join(output_folder, "%(title)s.%(ext)s"),  # Output file template
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",  # Extract audio using FFmpeg
                    "preferredcodec": "mp3",  # Convert to MP3
                    "preferredquality": "192",  # Audio quality
                },
                {
                    "key": "FFmpegThumbnailsConvertor",  # Download and convert thumbnail
                    "format": "jpg",  # Thumbnail format
                    "when": "before_dl",  # Download thumbnail before the video
                },
            ],
            "writethumbnail": True,  # Write thumbnail to disk
            "postprocessor_args": ["-vf", "thumbnail"],  # Thumbnail arguments
        }

        # Download the video and extract audio
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = sanitize_filename(info_dict.get("title", "audio"))
            thumbnail_url = info_dict.get("thumbnail", "")

        # Rename the downloaded files
        mp3_file = os.path.join(output_folder, f"{title}.mp3")
        thumbnail_file = os.path.join(output_folder, f"{title}_thumbnail.jpg")

        # Rename the thumbnail file
        if os.path.exists(os.path.join(output_folder, f"{title}.jpg")):
            os.rename(
                os.path.join(output_folder, f"{title}.jpg"),
                thumbnail_file,
            )

        print(f"Download complete: {mp3_file}")
        print(f"Thumbnail saved: {thumbnail_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Create a hidden root window for tkinter
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Use a GUI input dialog to get the YouTube URL
    youtube_url = simpledialog.askstring("Input", "Enter the YouTube video URL:")

    if youtube_url:
        download_youtube_audio(youtube_url)
    else:
        print("No URL provided. Exiting.")