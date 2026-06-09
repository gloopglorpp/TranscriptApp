# ====================================
# IMPORTS
# ====================================

from youtube_transcript_api import YouTubeTranscriptApi

from youtube_transcript_api._errors import IpBlocked, VideoUnavailable, TranscriptsDisabled, NoTranscriptFound

from pytubefix import Playlist, YouTube

import os

# ====================================
# FUNCTIONS
# ====================================

def extract_video_id(url):

    # Split the URL at "v=".
    # Everything after "v=" starts with the video ID.
    video_id_part = url.split("v=")[1]

    # Split again at "&".
    # This removes extra YouTube parameters like:
    # &list=...
    # &index=...
    video_id = video_id_part.split("&")[0]

    # Return only the clean video ID.
    return video_id

def download_transcript(video_id):

    # Create a transcript API object.
    ytt_api = YouTubeTranscriptApi()

    # Download transcript data and return it.
    return ytt_api.fetch(video_id)

def clean_transcript(transcript):

    # Create an empty string to store the final transcript.
    clean_text = ""

    # Loop through every transcript snippet.
    for entry in transcript:

        # Add the text from the snippet.
        clean_text += entry.text

        # Add a newline after each snippet.
        clean_text += "\n"

    # Return the completed transcript.
    return clean_text

def save_transcript(text, filename):

    with open(filename, "w") as file:
        file.write(text)

    # Display success message.
    print("Transcript saved to", filename)

def get_playlist_videos(playlist_url):

    playlist = Playlist(playlist_url)

    video_urls = list(playlist.video_urls)

    if len(video_urls) == 0:

        print("> WARNING: Playlist returned no videos.")

    return playlist.title, video_urls

def get_video_title(video_url):

    # Create a YouTube object.
    video = YouTube(video_url)

    # Return the video title.
    return video.title

def create_playlist_folder(playlist_name):

    # Create a folder for the playlist transcripts.
    folder_name = f"transcripts/{playlist_name}"

    os.makedirs(folder_name, exist_ok=True)

    return folder_name

# ====================================
# MAIN PROGRAM
# ====================================

print("=" * 50)

print("TRANSCRIPT APP")

print("=" * 50)

print()

# Display startup messages.

print("> CONNECTING TO TRANSCRIPT SYSTEM...")

print("> SYSTEM READY")

print()

# Display menu options.

print("1. Single Video")

print("2. Playlist")

print()

# Ask the user to choose an option.

choice = input("Select option: ")

# Check which option the user selected.
if choice == "1":

    print()
    print("> SINGLE VIDEO MODE SELECTED")

    youtube_url = input("Enter YouTube video URL: ")

    print("Processing...")

    video_id = extract_video_id(youtube_url)

    transcript = download_transcript(video_id)

    clean_text = clean_transcript(transcript)

    title = get_video_title(youtube_url)

    os.makedirs("transcripts/Single Videos", exist_ok=True)

    filename = f"transcripts/Single Videos/{title}.txt"

    save_transcript(clean_text, filename)

    print("> COMPLETE")

elif choice == "2":

    print()
    print("> PLAYLIST MODE SELECTED")

    playlist_url = input("Enter Playlist URL: ")

    playlist_title, videos = get_playlist_videos(playlist_url)

    folder_path = create_playlist_folder(playlist_title)

    print()
    print("> VIDEOS FOUND:", len(videos))

    for index, video in enumerate(videos, start=1):

        print()
        print("> PROCESSING VIDEO", index)
        print("> URL:", video)

        try:
            video_id = extract_video_id(video)

            transcript = download_transcript(video_id)

            clean_text = clean_transcript(transcript)

            title = get_video_title(video)

            filename = f"{folder_path}/{index:02d} - {title}.txt"

            save_transcript(clean_text, filename)

        except IpBlocked:
            print("> IP BLOCKED BY YOUTUBE")
            print("> STOPPING PLAYLIST TO AVOID MAKING IT WORSE")
            break

        except (VideoUnavailable, TranscriptsDisabled, NoTranscriptFound):
            print("> TRANSCRIPT NOT AVAILABLE FOR THIS VIDEO")
            print("> SKIPPING VIDEO")
            continue

        except Exception as error:
            print("> UNEXPECTED ERROR:")
            print(error)
            print("> SKIPPING VIDEO")
            continue

    print()
    print("> PLAYLIST COMPLETE")

else:

    print()
    print("> INVALID OPTION")