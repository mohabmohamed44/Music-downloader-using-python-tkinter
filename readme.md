
# Mp3 Music Downloader

## This Tkinter App built in Python allows you to download mp3 music from YouTube.

### Requirements
- Python 3.6 or higher
- yt-dlp
- tkinter
- ffmpeg
- ffprobe
- requests

#### Install requirements
* pip install -r requirements.txt

### Usage
1. Run the `main.py` script.
2. Enter the YouTube video URL in the input dialog.
3. The app will download the audio as an MP3 file and save the thumbnail.

### Project Structure
- `main.py`: Main script to run the application.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `requirements.txt`: List of dependencies to be installed.

### How it works
- The app uses `yt-dlp` to download the best quality audio from YouTube.
- The audio is converted to MP3 format using FFmpeg.
- The thumbnail is downloaded and saved as a JPEG file.
- The filenames are sanitized to remove invalid characters.

### License
This project is licensed under the MIT License.
