from database import get_toutes_questions, sauvegarder_score

def jouer_quiz():
    print("=" * 40)
    print("   BIENVENUE AU QUIZ GAME")
    print("=" * 40)

    joueur = input("\nEntrez votre nom: ")
    questions = get_toutes_questions()

    if not questions:
        print("Aucune question disponible!")
        return

    score = 0

    for q in questions:
        _, question, opt_a, opt_b, opt_c, bonne_reponse = q

        print(f"\n{question}")
        print(f"A) {opt_a}")
        print(f"B) {opt_b}")
        print(f"C) {opt_c}")

        reponse = input("Votre reponse (A/B/C): ").strip().upper()

        if reponse == bonne_reponse:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Faux! La bonne reponse etait: {bonne_reponse}")

    print("\n" + "=" * 40)
    pourcentage = (score / len(questions)) * 100
    print(f"Score final: {score}/{len(questions)} ({pourcentage:.0f}%)")

    if pourcentage == 100:
        print("🏆 Parfait! Tu es un champion!")
    elif pourcentage >= 60:
        print("👍 Bien joue!")
    else:
        print("💪 Continue à t'entraîner!")

    print("=" * 40)

    sauvegarder_score(joueur, score)
    print("Score enregistre!")