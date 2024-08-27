import pyttsx3
import time

def speak_with_custom_delay(text, global_delay):
    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Set the speech rate (default is usually around 200)
    engine.setProperty('rate', rate)


    # Split the text into words
    words = text.split()

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

if __name__ == "__main__":
    # Take text input from the user
    text = input("Enter the text you want to hear: (Paste your content) ")

    # Adjustable delay between words (in seconds)
    global_delay = float(input("Enter delay between words (in seconds e.g: 0.5 = 500ms): "))
    rate = int(input("Enter the reading speed (words per minute e.g: 150): "))

    # Speak the text with the specified delays
    speak_with_custom_delay(text, global_delay)
