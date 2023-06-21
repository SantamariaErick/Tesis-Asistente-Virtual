"""Configura el reconocimiento de voz: Usa la biblioteca de SpeechRecognition para configurar el reconocimiento de voz. 
Puedes usar el siguiente código para configurar el reconocimiento de voz y grabar el audio:"""
import speech_recognition as sr

#Mientras reconozca ruido se ejecutara ¿Problema en espacios concurridos, bulla ruido?
def recibe_audio(saludo):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(saludo)
        audio = r.listen(source)
    return audio

def reconoce_audio(audio):
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio, language='es-ES')
        print(f"Has dicho: {text}")
    except sr.UnknownValueError:
        print("No se ha podido entender lo que has dicho")
    except sr.RequestError as e:
        print("No se puede conectarse con el servicio de reconocimiento de voz; {0}".format(e))
    return text

def reconoce_audio_main(saludo):
    audio = recibe_audio(saludo)
    text = reconoce_audio(audio)
    return text


