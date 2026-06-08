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