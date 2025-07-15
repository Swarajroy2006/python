# Install an external module and use it to perform an operation of your interest.

from deep_translator import GoogleTranslator

input_text = input("Enter text to translate: ")

import pyttsx3
engine = pyttsx3.init()
engine.say(input_text+ " translated in Bengali")
engine.runAndWait()

translated = GoogleTranslator(source='auto', target='bn').translate(input_text)
print("Translated text:", translated)
# This code uses the deep_translator module to translate text from any language to Bengali.
