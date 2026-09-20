import sqlite3

def creer_connexion():
    """Ouvre une connexion vers le fichier quiz.db (le cree s'il n'existe pas)"""
    conn = sqlite3.connect('quiz.db')
    return conn


def creer_tables():
    """Cree les tables si elles n'existent pas deja"""
    conn = creer_connexion()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            bonne_reponse TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            joueur TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()


def ajouter_questions_de_base():
    """Ajoute des questions de depart dans la base (une seule fois)"""
    conn = creer_connexion()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM questions")
    nb_questions = cur.fetchone()[0]

    if nb_questions == 0:
        questions = [
            ("Quelle est la capitale de la Tunisie?", "Sfax", "Tunis", "Sousse", "B"),
            ("Combien font 5 + 7?", "10", "11", "12", "C"),
            ("Quel langage utilisons-nous ici?", "Java", "Python", "C++", "B"),
            ("Quelle planete est la plus proche du soleil?", "Venus", "Terre", "Mercure", "C"),
            ("Combien de continents existe-t-il?", "5", "7", "9", "B"),
        ]

        cur.executemany('''
            INSERT INTO questions (question, option_a, option_b, option_c, bonne_reponse)
            VALUES (?, ?, ?, ?, ?)
        ''', questions)

        conn.commit()
        print(f"{len(questions)} questions ajoutees!")
    else:
        print("Des questions existent deja dans la base.")

    conn.close()


def get_toutes_questions():
    """Recupere toutes les questions de la base"""
    conn = creer_connexion()
    cur = conn.cursor()
    cur.execute("SELECT * FROM questions")
    questions = cur.fetchall()
    conn.close()
    return questions


def sauvegarder_score(joueur, score):
    """Enregistre le score d'un joueur"""
    conn = creer_connexion()
    cur = conn.cursor()
    cur.execute("INSERT INTO scores (joueur, score) VALUES (?, ?)", (joueur, score))
    conn.commit()
    conn.close()


def get_classement():
    """Recupere le classement (meilleurs scores en premier)"""
    conn = creer_connexion()
    cur = conn.cursor()
    cur.execute("SELECT joueur, score, date FROM scores ORDER BY score DESC LIMIT 5")
    resultats = cur.fetchall()
    conn.close()
    return resultats


if __name__ == "__main__":
    creer_tables()
    ajouter_questions_de_base()
    print("Base de donnees prete!")