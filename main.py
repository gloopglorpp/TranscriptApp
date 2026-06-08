# Import the transcript library.
from youtube_transcript_api import YouTubeTranscriptApi


# Display application title.
print("Transcript App")


# Ask user for a YouTube URL.
youtube_url = input("Paste Youtube URL here: ")


# Tell the user we are processing.
print("Processing...")


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