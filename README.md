# Paragraph_Dictation_Script

Here's a `README.md` file for your project, including a description of the code and explanations for important lines.

# Text-to-Speech with Custom Delays

This Python script converts text to speech using the `pyttsx3` library, allowing users to specify a delay between words and adjust the speech rate. The script is particularly useful for dictation or practicing typing, as it provides ample time between words based on their length.

## Features

- **Custom Word Delay**: The user can set a global delay between each word. Additionally, the script calculates an extra delay based on the length of each word to provide more time for longer words.
- **Adjustable Speech Rate**: The user can set the speed of the speech in words per minute.
- **Text Input**: The script takes a string of text input and reads it aloud with the specified delays.

## Prerequisites

- Python 3.x
- `pyttsx3` library

Install `pyttsx3` using pip:

```bash
pip install pyttsx3
```

## How to Run

1. Clone the repository or download the script.
2. Run the script using Python:

```bash
python script_name.py
```

3. Enter the text you want to hear when prompted.
4. Specify the delay between words and the reading speed.

## Code Description

```python
import pyttsx3
import time
```

- **pyttsx3**: A text-to-speech conversion library in Python.
- **time**: A library that allows us to add delays between words.

```python
def speak_with_custom_delay(text, global_delay):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the speech rate (default is usually around 200)
    engine.setProperty('rate', rate)
```

- **engine = pyttsx3.init()**: Initializes the text-to-speech engine.
- **engine.setProperty('rate', rate)**: Sets the speech rate based on the user input. The default rate is typically around 200 words per minute.

```python
    # Split the text into words
    words = text.split()
```

- **text.split()**: Splits the input text into individual words, which will be spoken one at a time.

```python
    # Loop through the words and speak each one with a delay
    for word in words:
        engine.say(word)
        engine.runAndWait()
        
        # Calculate delay based on word length: 10ms per character
        word_delay = len(word) * 0.3  # 300ms per character
        
        # Add global delay between words
        time.sleep(global_delay)
        
        # Add the word-specific delay
        time.sleep(word_delay)
```

- **for word in words**: Iterates over each word in the text.
- **engine.say(word)**: Queues the word to be spoken.
- **engine.runAndWait()**: Processes the speech queue and speaks the word.
- **word_delay = len(word) * 0.3**: Calculates a delay based on the length of the word. Longer words will have a proportionally longer delay.
- **time.sleep(global_delay)**: Adds the global delay between words as specified by the user.
- **time.sleep(word_delay)**: Adds an additional delay based on the word's length.

```python
if __name__ == "__main__":
    # Take text input from the user
    text = input("Enter the text you want to hear: (Paste your content) ")

    # Adjustable delay between words (in seconds)
    global_delay = float(input("Enter delay between words (in seconds e.g: 0.5 = 500ms): "))
    rate = int(input("Enter the reading speed (words per minute e.g: 150): "))

    # Speak the text with the specified delays
    speak_with_custom_delay(text, global_delay)
```

- **if __name__ == "__main__":** Ensures that the script runs only when executed directly.
- **text = input("Enter the text...")**: Prompts the user to input the text they want to hear.
- **global_delay = float(input(...))**: Prompts the user to input the delay between words.
- **rate = int(input(...))**: Prompts the user to input the reading speed in words per minute.
- **speak_with_custom_delay(text, global_delay)**: Calls the function to start reading the text with the specified delays.

## License
This project is open-source and free to use.
