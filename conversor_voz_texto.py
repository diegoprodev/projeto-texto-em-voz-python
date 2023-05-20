from gtts import gTTS
import os


texto = input(f"bem vindo ao conversor de voz em texto, digite o que deseja ouvir: ")
language = "pt-br"

myobj = gTTS(text=texto,
             lang=language, slow=False)
myobj.save("bem vindo.mp3")
os.startfile("bem vindo.mp3")    

#time.sleep(3)
#diego rodrigues
    
