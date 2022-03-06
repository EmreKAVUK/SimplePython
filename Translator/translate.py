from googletrans import Translator
a = True
while a:
    text= input("Enter Your Message : ")
    if text == "exit" or text == "e":
        a = False
    else:
        translator = Translator()
        dt = translator.detect(text)
        translated = translator.translate(text)
        print(translated.text)

