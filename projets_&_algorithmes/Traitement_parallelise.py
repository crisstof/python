# Le multitraitement est une technique qui permet à un programme
# qui prend en charge plusieurs processeurs de répartir la charge
# Les applicarions dans le système multitraitements sont divisées en routines
# plus petites qui s'exécutent indépendamment
# le système alloue ces threads aux processeurs disponibles
import multiprocessing


def calcul_cube(num):
    print("Cube : {}".format(num * num * num))


def calcul_carre(num):
    print("Carre : {}".format(num * num))


if __name__ == "__main__":
    # création 1 processus
    p1 = multiprocessing.Process(target=calcul_cube, args=(10,))
    p2 = multiprocessing.Process(target=calcul_carre, args=(10,))
    # démarre le processus
    p1.start()
    p2.start()
    # attente de la fin du processus 1
    p1.join()
    # attente de la fin du processus 2
    p2.join()
    # les deux ont terminé
    print("Terminé")
