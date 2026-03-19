from gtts import gTTS
import os

print ("Welcome to the Text to Speech Converter!")
print ("Select language")

languages = [
    ('en', 'English', 'english'),
    ('es', 'Spanish', 'spanish'),
    ('fr', 'French', 'french'),
    ('de', 'German', 'german'),
    ('it', 'Italian', 'italian'),
    ('pt', 'Portuguese', 'portuguese'),
    ('ja', 'Japanese', 'japanese'),
    ('ko', 'Korean', 'korean'),
    ('zh', 'Chinese', 'chinese')
]

if lang in languages:
    print(f"Selected language: {i}")
else:
    print("Invalid language selection. Defaulting to English.")
    language = 'en'

def translation():
    print("Enter the text you want to convert to speech: ")
    text = input()
    f = open("text.txt", "w")
    f.write(text)
    f.close()
    
    f = open("text.txt", "r")
    
    input_text = f.read().replace("\n",'')
   
    
    language = 'en'

    voice = gTTS(text=input_text, lang=language, slow=False)

    voice.save("text.mp3")  

    os.system("start text.mp3")
    
    
    
    return input_text

if os.name == ('nt'):
    os.system('cls')

else:
    os.system('clear')

translation()
