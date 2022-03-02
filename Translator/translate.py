from googletrans import Translator
text="Naber kanka"
translator = Translator()
dt = translator.detect(text)
translated = translator.translate(text)
print(translated.text)