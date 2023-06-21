import pyttsx3
import nltk
import datetime

engine = pyttsx3.init()

def sintetizador_voz(saludo):
    engine.say(saludo)
    engine.runAndWait()

def procesar_respuesta(texto_reconocido):    
    # Procesamiento de una pregunta
    question = texto_reconocido
    tokens = nltk.word_tokenize(question)
    tags = nltk.pos_tag(tokens)
    lemmas = []
    for tag in tags:
        word = tag[0].lower()
        pos = tag[1][0].lower()
        if pos in ['a', 'n', 'v']:
            lemma = nltk.WordNetLemmatizer().lemmatize(word, pos)
            lemmas.append(lemma)
    question = " ".join(lemmas)

    # Generación de una respuesta
    if "cómo estás" in question:
        engine.say("Estoy bien, gracias por preguntar.")
    elif "qué hora es" in question:
        hora_actual = datetime.datetime.now().strftime("%H:%M")
        engine.say("Son las", hora_actual)

def sintetizador_voz_main(texto_reconocido, saludo):
    sintetizador_voz(saludo)
    procesar_respuesta(texto_reconocido)