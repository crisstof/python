import pygame
import random
import math

pygame.init()

# Configuration de l'écran
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tables de multiplication animées")

# Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Police
font = pygame.font.Font(None, 72)


def animate_numbers(a, b):
    clock = pygame.time.Clock()
    angle = 0
    for _ in range(60):  # Animation pendant 60 frames
        screen.fill(BLACK)

        # Animation du premier nombre
        text_a = font.render(str(a), True, WHITE)
        x_a = width // 4 + int(math.sin(angle) * 20)
        y_a = height // 2 + int(math.cos(angle) * 20)
        screen.blit(text_a, (x_a, y_a))

        # Animation du symbole de multiplication
        text_mul = font.render("x", True, WHITE)
        screen.blit(text_mul, (width // 2 - 20, height // 2 - 20))

        # Animation du deuxième nombre
        text_b = font.render(str(b), True, WHITE)
        x_b = 3 * width // 4 + int(math.cos(angle) * 20)
        y_b = height // 2 + int(math.sin(angle) * 20)
        screen.blit(text_b, (x_b, y_b))

        pygame.display.flip()
        angle += 0.1
        clock.tick(60)


def table_multiplication():
    running = True
    while running:
        a = random.randint(1, 10)
        b = random.randint(1, 10)

        animate_numbers(a, b)

        # Afficher la question
        screen.fill(BLACK)
        question = f"{a} x {b} = ?"
        text = font.render(question, True, WHITE)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 50))
        pygame.display.flip()

        # Attendre la réponse de l'utilisateur
        answer = ""
        waiting_for_answer = True
        while waiting_for_answer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting_for_answer = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waiting_for_answer = False
                    elif event.key == pygame.K_BACKSPACE:
                        answer = answer[:-1]
                    elif event.unicode.isdigit():
                        answer += event.unicode

            # Afficher la réponse en cours
            screen.fill(BLACK)
            screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - 50))
            answer_text = font.render(answer, True, BLUE)
            screen.blit(
                answer_text,
                (width // 2 - answer_text.get_width() // 2, height // 2 + 50),
            )
            pygame.display.flip()

        # Vérifier la réponse
        if answer and int(answer) == a * b:
            result = "Correct !"
        else:
            result = f"Incorrect. La réponse était {a * b}."

        # Afficher le résultat
        screen.fill(BLACK)
        result_text = font.render(result, True, WHITE)
        screen.blit(
            result_text, (width // 2 - result_text.get_width() // 2, height // 2)
        )
        pygame.display.flip()

        # Attendre 2 secondes avant la prochaine question
        pygame.time.wait(2000)

    pygame.quit()


table_multiplication()
