import pywhatkit as kit
import cv
msg = input('Enter your input')
kit.text_to_handwriting(msg , save_to="elyazisi.png")
