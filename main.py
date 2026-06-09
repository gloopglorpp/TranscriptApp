# ====================================
# IMPORTS
# ====================================

from youtube_transcript_api import YouTubeTranscriptApi

# ====================================
# FUNCTIONS
# ====================================

def extract_video_id(url):

    # Split the URL at "=" and return the second part.
    return url.split("=")[1]

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

def save_transcript(text):

    # Open transcript.txt in write mode.
    with open("transcript.txt", "w") as file:

        # Write the transcript text into the file.
        file.write(text)

    # Display success message.
    print("Transcript saved to transcript.txt")

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

elif choice == "2":

    print()
    print("> PLAYLIST MODE SELECTED")

else:

    print()
    print("> INVALID OPTION")

# Extract the video ID from the URL.
video_id = extract_video_id(youtube_url)

transcript = download_transcript(video_id)

clean_text = clean_transcript(transcript)

save_transcript(clean_text)

print("> COMPLETE")