import random

def jugar_piedra_papel_tijera(jugador, computadora):
    if jugador == computadora:
        return "Es un empate"
    elif (jugador == "piedra" and computadora == "tijera") or (jugador == "papel" and computadora == "piedra") or (jugaodr == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"

opciones = ["piedra", "papel", "tijera"]
jugador = input("Elige piedra, papel o tijera: ").lower()

if jugador in opciones: 
    computadora = random.choice(opciones)
    print(f"La computadora eligio: {computadora}")
    resultado = jugar_piedra_papel_tijera(jugador, computadora)
    print(resultado)
else:
    print("Entrada inválida! Por favor, elige piedra, papel o tijera")
