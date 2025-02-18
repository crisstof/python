import random


def table_multiplication():
    print("Bienvenue dans le jeu des tables de multiplication !")

    while True:
        # Choisir deux nombres aléatoires entre 1 et 10
        a = random.randint(1, 10)
        b = random.randint(1, 10)

        # Poser la question
        print(f"\nQuelle est le résultat de {a} x {b} ?")

        # Demander la réponse à l'utilisateur
        reponse_utilisateur = input("Votre réponse : ")

        # Vérifier si la réponse est un nombre
        try:
            reponse_utilisateur = int(reponse_utilisateur)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        # Vérifier la réponse
        if reponse_utilisateur == a * b:
            print("Bravo ! C'est la bonne réponse.")
        else:
            print(f"Désolé, la bonne réponse était {a * b}.")

        # Demander si l'utilisateur veut continuer
        continuer = input("\nVoulez-vous continuer ? (o/n) : ")
        if continuer.lower() != "o":
            break

    print("Merci d'avoir joué !")


# Lancer le jeu
table_multiplication()
