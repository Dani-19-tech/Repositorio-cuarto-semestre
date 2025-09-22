#En un juego de preguntas a las que se responde “Sí” o “No” gana quien responda correctamente las tres preguntas. Si se responde mal a cualquiera de ellas, ya no se pregunta la siguiente y termina el juego. Las preguntas son:
#Colón descubrió América?
#La independencia de Colombia fue en el año 1810?
#The Doors fue un grupo de rock Americano? # Juego de preguntas de Sí o No

print("Responde con 'si' o 'no' a las siguientes preguntas.\n")

# Primera pregunta
respuesta1 = input("1. ¿Colón descubrió América? ")

if respuesta1 == "si":
    # Segunda pregunta
    respuesta2 = input("2. ¿La independencia de Colombia fue en el año 1810? ").lower()
    if respuesta2 == "si":
        # Tercera pregunta
        respuesta3 = input("3. ¿The Doors fue un grupo de rock Americano? ").lower()
        if respuesta3 == "si":
            print("\n¡Felicidades! Respondiste correctamente las tres preguntas 🎉")
        else:
            print("\nRespuesta incorrecta. Fin del juego ")
    else:
        print("\nRespuesta incorrecta. Fin del juego ")
else:
    print("\nRespuesta incorrecta. Fin del juego ")
