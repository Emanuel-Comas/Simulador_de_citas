import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ANCHO, ALTO = 800, 500
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Simulador de Citas")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)

# Fuente
fuente = pygame.font.Font(None, 36)

# Personajes
personajes = ["Alice", "Anya", "Rikka", "Tanya", "Miku"]
opciones_cita = ["Ir a un restaurante", "Hacer una caminata por el parque", "Ver una película", "Ponerse a programar"]

def dibujar_texto(texto, x, y):
    texto_superior = fuente.render(texto, True, NEGRO)
    pantalla.blit(texto_superior, (x, y))

def seleccionar_personaje():
    pantalla.fill(BLANCO)
    dibujar_texto("Elige un personaje:", 50, 50)

    for i, personaje in enumerate(personajes):
        dibujar_texto(f"{i + 1}. {personaje}", 50, 100 + i * 40)

    pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5):
                    return personajes[evento.key - pygame.K_1]

def cita(personaje):
    pantalla.fill(BLANCO)
    dibujar_texto(f"Has elegido a {personaje}.", 50, 50)
    dibujar_texto("Elige una actividad:", 50, 100)

    for i, opcion in enumerate(opciones_cita):
        dibujar_texto(f"{i + 1}. {opcion}", 50, 150 + i * 40)

    pygame.display.flip()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4):
                    return opciones_cita[evento.key - pygame.K_1]

def resultado_cita(opcion, personaje):
    resultados = {
        "Ir a un restaurante": [
            f"{personaje} disfrutó de la cena y te dio un abrazo.",
            f"La cena fue un desastre, pero ambos se rieron."
        ],
        "Hacer una caminata por el parque": [
            f"{personaje} se sintió inspirado por la naturaleza.",
            f"Perdiste la noción del tiempo en una conversación profunda."
        ],
        "Ver una película": [
            f"{personaje} amó la película y quieren ver otra juntos.",
            f"No disfrutaron la película, pero se divirtieron comentándola."
        ], 
        "Ponerse a programar":[
            f"{personaje} le gusto como le enseñaste a programar.",
            f"No logra entender bien la orientacion a objetos"
        ]
    }

    resultado = random.choice(resultados[opcion])
    return resultado

def main():
    while True:
        personaje = seleccionar_personaje()
        opcion = cita(personaje)

        pantalla.fill(BLANCO)
        resultado = resultado_cita(opcion, personaje)
        dibujar_texto(f"Resultado: {resultado}", 50, 50)

        pygame.display.flip()
        pygame.time.wait(3000)  # Espera 3 segundos antes de reiniciar

if __name__ == "__main__":
    main()
