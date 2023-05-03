from reconocimiento_voz import * #Importa todo lo que hay en el archivo reconocimiento_voz.py
from sintetizador_voz import * #Importa todo lo que hay en el archivo sintetizador_voz.py

def main():
    saludo = "Hola soy tu asistente virtual, ¿en qué puedo ayudarte?"
    text = reconoce_audio_main(str(saludo))
    sintetizador_voz_main(str(text), str(saludo))
main()
