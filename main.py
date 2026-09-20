from database import creer_tables, ajouter_questions_de_base, get_classement
from quiz import jouer_quiz

def afficher_menu():
    print("\n" + "=" * 40)
    print("        QUIZ GAME - MENU")
    print("=" * 40)
    print("1. Jouer")
    print("2. Voir le classement")
    print("3. Quitter")

def main():
    # Prepare la base de donnees au demarrage
    creer_tables()
    ajouter_questions_de_base()

    while True:
        afficher_menu()
        choix = input("\nVotre choix: ")

        if choix == "1":
            jouer_quiz()
        elif choix == "2":
            print("\n--- CLASSEMENT (Top 5) ---")
            classement = get_classement()
            if not classement:
                print("Aucun score enregistre pour le moment.")
            else:
                for i, (joueur, score, date) in enumerate(classement, start=1):
                    print(f"{i}. {joueur} - {score} points ({date})")
        elif choix == "3":
            print("A bientot!")
            break
        else:
            print("Choix invalide, reessayez.")

if __name__ == "__main__":
    main()