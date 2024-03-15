import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import googletrans
from gtts import gTTS
import os
import sounddevice as sd
import soundfile as sf
import pygame

def translate_text():
    # Get text from input field
    input_text = input_entry.get()
    # Translate text using Google Translate API
    translator = googletrans.Translator()
    translated_text = translator.translate(input_text, src='en', dest='vi').text

    # Update result text
    result_label.config(text=translated_text)


def speech_to_text():
    status_label.config(text="Đang thu âm...")
    root.update()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            recognized_text = r.recognize_google(audio)
            input_entry.delete(0, tk.END)
            input_entry.insert(tk.END, recognized_text)
        except sr.UnknownValueError:
            print("Could not understand audio")
            status_label.config(text="Không thể hiểu được âm thanh")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            status_label.config(text="Không thể yêu cầu kết quả")
    status_label.config(text="")


def play_audio():
    # Initialize pygame mixer
    pygame.mixer.init()

    # Play audio from input field
    input_text = input_entry.get()
    translator = googletrans.Translator()
    translated_text = translator.translate(input_text, src='en', dest='vi').text
    tts = gTTS(translated_text, lang='vi')
    tts.save('output.mp3')

    # Load audio file
    pygame.mixer.music.load('output.mp3')

    # Play audio
    pygame.mixer.music.play()

def exit_program():
    root.destroy()
# Create main window
root = tk.Tk()
root.title("Translator")

# Create input label and entry
input_label = ttk.Label(root, text="Enter text:")
input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_entry = ttk.Entry(root, width=40)
input_entry.grid(row=0, column=1, padx=5, pady=5)

# Create translate button
translate_button = ttk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=0, column=2, padx=5, pady=5)

# Create result label
result_label = ttk.Label(root, text="")
result_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Create speech to text button
speech_to_text_button = ttk.Button(root, text="Speech to Text", command=speech_to_text)
speech_to_text_button.grid(row=2, column=0, padx=5, pady=5)

# Create play audio button
play_audio_button = ttk.Button(root, text="Play Audio", command=play_audio)
play_audio_button.grid(row=2, column=1, padx=5, pady=5)

#create exit button
exit_button = ttk.Button(root, text="Exit", command=exit_program)
exit_button.grid(row=2, column=2, padx=5, pady=5)

#creatr status label
status_label = ttk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Start GUI main loop
root.mainloop()
