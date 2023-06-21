"""
from reconocimiento_voz import * #Importa todo lo que hay en el archivo reconocimiento_voz.py
from sintetizador_voz import * #Importa todo lo que hay en el archivo sintetizador_voz.py

def main():
    saludo = "Hola soy tu asistente virtual, ¿en qué puedo ayudarte?"
    text = reconoce_audio_main(str(saludo))
    sintetizador_voz_main(str(text), str(saludo))
main()
"""

# Importar los módulos necesarios
import speech_recognition as sr
import pyttsx3

# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()

# Crear un objeto de síntesis de voz
engine = pyttsx3.init()

# Definir una función para responder preguntas
def responder(pregunta):
  # Aquí se puede agregar la lógica para buscar la respuesta en internet o en una base de datos
  # Por ejemplo, se puede usar el módulo wikipedia para buscar información en la enciclopedia
  # import wikipedia
  # wikipedia.set_lang("es")
  # respuesta = wikipedia.summary(pregunta, sentences=1)
  
  # Para simplificar, vamos a usar unas respuestas predefinidas
  respuestas = {
    "matriculas espe": "Documentación Primer Nivel. Copia de cédula de identidad y certificado  de votación. Copia certificada por cualquier Notaria del Acta de Grado o Título de Bachiller debidamente refrendado por el Ministerio de Educación (Dirección distrital). Hoja de datos personales con fotografía de frente, tamaño carné a color. Respaldo Puntaje SENESCYT. La certificación médica, podrá ser emitida por un facultativo de la Universidad de las Fuerzas Armadas ESPE o por un centro  de salud público. Copia simple del carné  de discapacidad del CONADIS o del certificado del Ministerio de Salud Pública (Aplica únicamente para personas con discapacidad).",
    "qué hora es": "Son las cinco y cincuenta y siete de la tarde.",
    "cuál es el sentido de la vida": "Esa es una pregunta muy profunda. Algunas personas pueden pensar que el sentido de la vida es ser feliz, otras que es cumplir una misión o un propósito. No hay una respuesta única o definitiva."
  }

  # Buscar la pregunta en el diccionario de respuestas
  if pregunta in respuestas:
    # Si se encuentra, devolver la respuesta correspondiente
    return respuestas[pregunta]
  else:
    # Si no se encuentra, devolver una respuesta genérica
    return "Lo siento, no puedo responder a esa pregunta."

# Definir una función para escuchar y procesar el audio del micrófono
def escuchar():
  # Usar el micrófono como fuente de audio
  with sr.Microphone() as source:
    # Ajustar el nivel de ruido ambiental
    r.adjust_for_ambient_noise(source)
    # Indicar al usuario que puede hablar
    print("Puedes hablar ahora.")
    # Escuchar el audio del micrófono
    audio = r.listen(source)
  
  try:
    # Intentar reconocer el audio usando el idioma español
    texto = r.recognize_google(audio, language="es-ES")
    # Devolver el texto reconocido
    return texto
  except:
    # Si ocurre algún error, devolver None
    return None

# Definir una función para hablar y reproducir el audio por los parlantes
def hablar(texto):
  # Establecer el idioma y el género de la voz
  engine.setProperty("voice", "spanish")
  engine.setProperty("gender", "female")
  # Decir el texto
  engine.say(texto)
  # Esperar a que se termine de reproducir el audio
  engine.runAndWait()

# Iniciar el asistente virtual
print("Bienvenido al asistente virtual. Puedes hacerme preguntas simples y trataré de responderlas.")
hablar("Bienvenido al asistente virtual. Puedes hacerme preguntas simples y trataré de responderlas.")

# Crear un bucle para escuchar y responder preguntas hasta que el usuario diga adiós
while True:
  # Escuchar la pregunta del usuario
  pregunta = escuchar()
  # Si se reconoció algún texto, procesarlo
  if pregunta is not None:
    # Mostrar la pregunta en la pantalla
    print("Pregunta:", pregunta)
    # Si la pregunta es adiós, terminar el bucle y despedirse
    pregunta = pregunta.lower()
    if pregunta == "adiós":
      print("Respuesta: Adiós, que tengas un buen día.")
      hablar("Adiós, que tengas un buen día.")
      break
    else:
      # Si no, buscar la respuesta y mostrarla en la pantalla
      respuesta = responder(pregunta)
      print("Respuesta:", respuesta)
      # Hablar la respuesta por los parlantes
      hablar(respuesta)
