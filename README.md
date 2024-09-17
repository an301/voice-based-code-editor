# Voice-Based Code Editor

This project provides a voice-based interface for coding, allowing users to dictate Python code and see it executed in real-time. It uses speech recognition to convert spoken commands into Python code, which can then be run in a web-based environment.

## Key Features

- Converts speech to Python code using the `speech_recognition` library and Google Speech API.
- Supports spoken commands for symbols (e.g., "open parentheses," "semicolon").
- Displays the code and output after recording and submitting the command.

## Usage

1. Install the necessary dependencies: `flask`, `speech_recognition`, and `subprocess` via your project interpreter.
2. Run `app.py` to start the Flask server.
3. Navigate to the audio test page:
   - Hit the Record button.
   - After speaking, click Stop and then Submit.
   - You will be redirected to a page displaying the code and its output (supports one-liners).

## Future Considerations

- **Design Choice**: The current implementation focuses on simplicity and execution of single-line code snippets, but it could be enhanced to handle multi-line code blocks with improved parsing.
  
- **Code Execution**: Expanding to support additional languages and improve execution for more complex Python code. A secure sandboxed environment could prevent unsafe code execution.

- **Real-time Feedback**: Implement live error checking and feedback during dictation.
