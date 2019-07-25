
import speech_recognition as sr

def Monitora_microfone():
    #https://github.com/Uberi/speech_recognition#readme
    #https: // github.com / Uberi / speech_recognition / blob / master / reference / library - reference.rst
    # obtain audio from the microphone
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diaga algo a Yaga")
        audio = microfone.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("Yaga acha que você disse: " + microfone.recognize_google(audio,language='pt-BR'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))