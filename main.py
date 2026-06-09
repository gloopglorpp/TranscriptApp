# Import the transcript library.
from youtube_transcript_api import YouTubeTranscriptApi


# Display a title banner.

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
video_id = youtube_url.split("=")[1]


# Create a transcript API object.
ytt_api = YouTubeTranscriptApi()


# Download transcript data.
transcript = ytt_api.fetch(video_id)


# Create an empty string.
#
# We will gradually add transcript text to this variable.
clean_transcript = ""


# Loop through every transcript entry.
#
# Each entry contains:
# text
# start
# duration
for entry in transcript:

    # Take only the text portion.
    #
    # Example:
    # entry["text"]
    #
    # might return:
    # "Hello everyone"
    clean_transcript += entry.text

    # Add a newline after each transcript line.
    clean_transcript += "\n"

# Open a file named transcript.txt.
#
# "w" means write mode.
# If the file already exists, it will be overwritten.
with open("transcript.txt", "w") as file:

    # Write the cleaned transcript into the file.
    file.write(clean_transcript)


# Tell the user the file was created.
print("Transcript saved to transcript.txt")

# Print the cleaned transcript.
print(clean_transcript)