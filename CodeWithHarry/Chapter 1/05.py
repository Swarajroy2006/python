# Label the program written in problem 4 with comments.

# Install an external module and use it to perform an operation of your interest.

from deep_translator import GoogleTranslator
# pip install googletrans==4.0.0-rc1 gTTS
import pyttsx3
# pip install pyttsx3

input_text = input("Enter text to translate: ")

import pyttsx3
engine = pyttsx3.init()
engine.say(input_text+ " translated in Bengali")
engine.runAndWait()

translated = GoogleTranslator(source='auto', target='bn').translate(input_text)
print("Translated text:", translated)
# This code uses the deep_translator module to translate text from any language to Bengali.
# The program initializes a text-to-speech engine and translates user input into Bengali.
# It also reads the translated text aloud using the pyttsx3 module.