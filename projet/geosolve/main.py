
import math
import time


def distance_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) #math.sqrt() permet de calculer une racine carré


def milieu_segment(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y


def resoudre_second_degre(a, b, c):
    if a == 0:
        return "Ce n'est pas une équation du second degré."

    delta = b**2 - 4*a*c

    if delta < 0:
        return "Aucune solution réelle."
    elif delta == 0:
        x = -b / (2*a)
        return  f"Une solution : x = {x}"
    else:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return f"Deux solutions : x1 = {x1}, x2 = {x2}"


def est_proche_zero(valeur, echelle, epsilon=1e-10):
    return abs(valeur) <= epsilon * echelle


def intersection_droites(a1, b1, c1, a2, b2, c2):
    # Vérifier que les deux équations représentent bien des droites
    if (a1 == 0 and b1 == 0) or (a2 == 0 and b2 == 0):
        return "Erreur : une équation ne représente pas une droite."

    # Calcul du déterminant principal
    determinant = a1 * b2 - a2 * b1

    # Échelle utilisée pour évaluer la précision du déterminant
    echelle = abs(a1 * b2) + abs(a2 * b1)

    if est_proche_zero(determinant, echelle):
        # Déterminants secondaires
        dx = c1 * b2 - c2 * b1
        dy = a1 * c2 - a2 * c1

        echelle_dx = abs(c1 * b2) + abs(c2 * b1)
        echelle_dy = abs(a1 * c2) + abs(a2 * c1)

        if (est_proche_zero(dx, echelle_dx)
                and est_proche_zero(dy, echelle_dy)):
            return "Les droites sont confondues."

        return "Les droites sont parallèles ou presque parallèles."

    # Calcul des coordonnées du point d'intersection
    x = (c1 * b2 - c2 * b1) / determinant
    y = (a1 * c2 - a2 * c1) / determinant

    return f"Point d'intersection : ({x}, {y})"

def lancer_experiences():
    cas = [
        ("Droites secantes", 1, 1, 5, 1, -1, 1),
        ("Droites paralleles", 1, 1, 5, 1, 1, 8),
        ("Droites confondues", 1, 1, 5, 2, 2, 10),
        ("Droites presque paralleles", 1, 1, 2, 1, 1.00000000001, 3)
    ]

    for experience in cas:
        nom = experience[0]
        a1 = experience[1]
        b1 = experience[2]
        c1 = experience[3]
        a2 = experience[4]
        b2 = experience[5]
        c2 = experience[6]

        determinant = a1 * b2 - a2 * b1
        echelle = abs(a1 * b2) + abs(a2 * b1)
        seuil = 1e-10 * echelle

        print("\n---", nom, "---")
        print("Determinant :", determinant)
        print("Seuil de tolerance :", seuil)

        resultat = intersection_droites(a1, b1, c1, a2, b2, c2)
        print("Resultat :", resultat)


def menu():# permet utiliser le programe sans modifier le code
    while True:
        print("\n========== GEOSOLVE ==========")
        print("1. Calculer une distance")
        print("2. Calculer le milieu d'un segment")
        print("3. Résoudre une équation du second degré")
        print("4. Trouver l'intersection de deux droites")
        print("5. Lancer les experiences numeriques")
        print("6. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            x1 = float(input("x1 : "))
            y1 = float(input("y1 : "))
            x2 = float(input("x2 : "))
            y2 = float(input("y2 : "))

            debut = time.perf_counter()
            resultat = distance_points(x1, y1, x2, y2)
            duree = time.perf_counter() - debut

            print("Distance :", resultat)
            print("Temps de calcul :", duree, "secondes")

        elif choix == "2":
            x1 = float(input("x1 : "))
            y1 = float(input("y1 : "))
            x2 = float(input("x2 : "))
            y2 = float(input("y2 : "))

            print("Milieu :", milieu_segment(x1, y1, x2, y2))

        elif choix == "3":
            a = float(input("Coefficient a : "))
            b = float(input("Coefficient b : "))
            c = float(input("Coefficient c : "))

            print(resoudre_second_degre(a, b, c))

        elif choix == "4":
            print("Première droite : a1*x + b1*y = c1")
            a1 = float(input("a1 : "))
            b1 = float(input("b1 : "))
            c1 = float(input("c1 : "))

            print("Deuxième droite : a2*x + b2*y = c2")
            a2 = float(input("a2 : "))
            b2 = float(input("b2 : "))
            c2 = float(input("c2 : "))

            print(intersection_droites(a1, b1, c1, a2, b2, c2))

        elif choix == "5":
            lancer_experiences()

        elif choix == "6":
            print("Merci d'avoir utilise GeoSolve !")
            break    

       

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
