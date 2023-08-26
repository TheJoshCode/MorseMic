import speech_recognition as sr
import time
import sounddevice as sd
import numpy as np
import os

os.system("pip install speechrecognition sounddevice")
os.system("cls")

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
    return ' '.join(morse_code)

def play_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            duration = 0.2
        elif symbol == '-':
            duration = 0.6
        elif symbol == ' ':
            time.sleep(0.3)  # Pause between characters
            continue
        elif symbol == '/':
            time.sleep(0.7)  # Pause between words
            continue
        
        frequency = 800
        volume = 0.1
        samples = int(duration * 44100)
        t = np.linspace(0, duration, samples, False)
        signal = np.sin(2 * np.pi * frequency * t) * volume
        sd.play(signal, 44100)
        sd.wait()

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        while True:
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                morse_code = text_to_morse(text)
                
                print(f"You said: {text}")
                print(f"Morse code: {morse_code}")
                
                play_morse_code(morse_code)
                
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")

if __name__ == "__main__":
    main()




