# Import the YouTubeTranscriptApi class from the installed package.
# This gives our program access to transcript-related functionality
# written by the creators of the library.
from youtube_transcript_api import YouTubeTranscriptApi


# Display a startup message so we know the import succeeded.
print("Import successful")

# Display the application title.
print("Transcript App")


# Ask the user to paste a YouTube URL.
# input() pauses the program and waits for keyboard input.
# Whatever the user types is returned as a string and stored
# inside the youtube_url variable.
youtube_url = input("Paste Youtube URL here: ")


# Inform the user that the program is now doing work.
print("Processing...")


# Split the URL into pieces using "=" as the separator.
#
# Example:
# https://www.youtube.com/watch?v=sD0NjbwqlYw
#
# becomes:
#
# [
#     "https://www.youtube.com/watch?v",
#     "sD0NjbwqlYw"
# ]
#
# [1] means:
# "Give me the second item in the list."
#
# The second item is the video ID.
video_id = youtube_url.split("=")[1]


# Display the extracted video ID.
# This lets us verify that our extraction logic worked.
print("Video ID:", video_id)


# Create an instance (object) of the YouTubeTranscriptApi class.
#
# Think of the class as a blueprint.
# This line creates a real object we can use.
ytt_api = YouTubeTranscriptApi()


# Ask the object to fetch the transcript for the video ID.
#
# The returned transcript is stored in the transcript variable.
#
# At this stage we don't know exactly what data structure
# the library returns, so we're going to inspect it.
transcript = ytt_api.fetch(video_id)


# Print whatever transcript data was returned.
#
# This is a debugging step.
# We want to see the structure of the data before deciding
# how to process it.
print(transcript)