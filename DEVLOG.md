# Development Journal

## 2026-06-08 — Project Initialization

Today I created the foundation for the Transcript App project. The goal of the project is to create a tool capable of downloading YouTube transcripts and eventually converting them into study flashcards.

The initial focus is not on artificial intelligence or flashcard generation. Instead, the goal is to build the application incrementally while learning Python, Git, software structure, and project development practices.

I created a local Git repository, made the first commit, and connected the project to GitHub. This establishes version control from the beginning and allows progress to be tracked throughout development.

The project currently contains a README file, a .gitignore file, and a basic Python entry point. No application functionality has been implemented yet.

The next milestone will be accepting a YouTube URL from the user and beginning to process it.

### Lessons Learned

- Git repositories should be initialized inside the project folder, not from the root filesystem.
- GitHub repositories and local Git repositories are separate until connected with a remote.
- Commits create snapshots of a project's state that can be revisited later.
- Establishing version control early creates a safer environment for experimentation and learning.
- Small, incremental milestones are easier to test and understand than building large features all at once.

## 2026-06-08 — Implemented user input handling.

The application can now accept a YouTube URL from the terminal and store it in a variable for future processing.

Lessons Learned:
- input() waits for user input and returns a string.
- Variables can store user-provided data.
- print() can output both strings and variables.

## 2026-06-08 — Video ID Extraction

Implemented YouTube video ID extraction.

The program now accepts a YouTube URL and uses Python's split("=") method to separate the URL into parts. The video ID is retrieved from the second item in the resulting list using index [1].

### Lessons Learned

- Strings can be split into lists using split().
- Lists use zero-based indexing.
- Useful information can be extracted from text by identifying patterns.
- User input can be transformed into data for later processing.

## 2026-06-08 — Transcript Retrieval

Implemented transcript retrieval from YouTube videos.

Created a Python virtual environment for the project and installed the youtube-transcript-api package. Learned how Python imports external libraries and how third-party packages can add functionality to a program.

Used the extracted YouTube video ID to request a transcript from YouTube. Encountered an error when using an outdated method name and used Python's dir() function to inspect the available methods within the library. Discovered that the current version uses fetch() rather than get_transcript().

Successfully downloaded transcript data for a YouTube video and displayed the returned data structure in the terminal.

### Lessons Learned

- Virtual environments isolate project dependencies from the rest of the system.
- External packages can be installed using pip.
- Libraries change over time, and online tutorials may contain outdated code.
- dir() can be used to inspect available attributes and methods of an object.
- Classes act as blueprints and must often be instantiated before use.
- Methods can return complex data structures that may need further processing.
- Debugging often involves investigating what a program is actually receiving rather than guessing.

## 2026-06-08 — Transcript Cleaning and File Export

Implemented transcript cleaning and file export functionality.

After successfully retrieving transcript data from YouTube, I processed the returned transcript objects to extract only the spoken text. This removed timestamps and other metadata, producing a clean, readable transcript.

Introduced a for loop to iterate through each transcript snippet and used object attributes to access the transcript text. The individual transcript lines were combined into a single string representing the complete transcript.

The application can now save the cleaned transcript to a text file named transcript.txt, creating a permanent output file instead of displaying large amounts of text in the terminal.

### Lessons Learned

- Loops can process collections of objects one item at a time.
- Objects expose data through attributes using dot notation.
- Strings can be built incrementally during processing.
- Files can be created and written using Python's open() function.
- The with statement automatically handles file closing and cleanup.
- Program output can be transformed into reusable files rather than temporary terminal output.

## 2026-06-09 — Terminal Menu System

Added a terminal-based menu system to the application.

Users can now select between Single Video and Playlist modes. Single Video mode has been fully integrated with the transcript pipeline, allowing a YouTube URL to be processed from start to finish.

The application now downloads a transcript, removes metadata, converts it into readable text, and saves the result as a text file. This marks the first complete workflow within the project.

### Lessons Learned

- Conditional statements allow programs to follow different paths based on user input.
- Menu systems provide a simple way to organize application functionality.
- Features should be integrated incrementally and tested after each change.
- Text data can be transformed and saved as reusable files.
- A working terminal interface can be built before creating a graphical user interface.

## 2026-06-09 — Refactoring Into Functions

Refactored the transcript processing workflow into reusable functions.

Previously, the application contained all logic directly within the main program flow. To improve readability and prepare for future features such as playlist processing, the transcript workflow was separated into distinct functions.

Created functions for:

- Extracting a YouTube video ID from a URL
- Downloading transcript data from YouTube
- Converting transcript objects into clean text
- Saving transcript text to a file

The main program now acts as a high-level controller, calling functions in sequence rather than containing the implementation details itself. This makes the code easier to understand, maintain, and expand.

### Lessons Learned

- Functions allow code to be broken into smaller, reusable units.
- Functions can accept inputs through parameters and return outputs using return.
- Refactoring improves code organization without changing program behaviour.
- Separating responsibilities makes future features easier to implement.
- Well-named functions can make a program read almost like plain English.
- Large projects become easier to manage when implementation details are hidden behind reusable functions.

## 2026-06-09 — Playlist Support Foundation

Expanded the application architecture to support future playlist processing.

Integrated the pytubefix library and created functionality for retrieving video URLs from YouTube playlists. Refactored transcript saving to accept custom filenames, preparing the application to save multiple transcripts without overwriting existing files.

Improved the overall program structure by separating single-video and playlist workflows and continuing to build functionality around reusable functions.

During testing, discovered issues involving SSL certificates, URL parsing, and playlist processing. These were investigated and resolved incrementally, reinforcing the importance of debugging and testing after each change.

### Lessons Learned

- Functions make large features easier to build incrementally.
- Third-party libraries can introduce environment-specific issues unrelated to application logic.
- URLs often contain additional parameters that must be cleaned before processing.
- Program flow should be separated so different menu options execute independent workflows.
- Refactoring early makes future expansion significantly easier.
- Debugging often involves isolating whether the problem is code, data, a library, or the development environment.

## 2026-06-09 — Playlist Transcript Support

Added playlist processing functionality to the application.

The program can now accept a YouTube playlist URL, retrieve all available video URLs from the playlist, and automatically process each video. For every video found, the transcript is downloaded, cleaned, and saved as a separate text file.

This marks the first multi-item automation workflow in the project, moving beyond single-video processing.

### Lessons Learned

- Functions become increasingly valuable as projects grow.
- Loops allow the same workflow to be applied repeatedly to many items.
- Playlist data can be retrieved and processed programmatically.
- URL parsing is important when working with real-world web links.
- Debugging often involves distinguishing between code issues and third-party library behaviour.

## 2026-06-09 — Improved Playlist Export System

Enhanced the playlist export workflow to produce more meaningful and organized transcript files.

Instead of saving playlist transcripts using generic names such as transcript_1.txt and transcript_2.txt, the application now retrieves each video's title and uses it as the filename. This makes exported transcripts immediately identifiable without needing to open them.

Also added automatic transcript folder creation. All exported transcript files are now stored inside a dedicated transcripts directory rather than cluttering the project root.

### Lessons Learned

- External data can be used to generate more user-friendly filenames.
- Functions can be expanded and reused without affecting the rest of the program.
- Programs can automatically create folders using os.makedirs().
- Organizing generated files becomes increasingly important as a project grows.
- Small quality-of-life improvements can significantly improve the user experience.
- Separating application files from generated output leads to a cleaner project structure.

