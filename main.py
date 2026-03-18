from gtts import gTTS
import os

if os == ('nt'):
    os.system('cls')
else:
    os.system('clear')

language = 'en'

f = open("text.txt", "r")

input_text = f.read().replace("\n",'')

language = 'en'

voice = gTTS(text=input_text, lang=language, slow=False)

voice.save("text.mp3")  

os.system("start text.mp3")