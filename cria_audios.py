#Texto para voz
from gtts import gTTS
#from subprocess import call #Mac e Linux
from playsound import playsound  #Windows


def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audio/hello.mp3')
    #call(['afplay','audio/estou_bem.mp3']) # Chamada para MAC
    #call(['aplay','audio/hello.mp3']) #Chamada para Linux
    playsound('audio/hello.mp3') #chamado para Windows


cria_audio('Olá, meu nome é Yaga')