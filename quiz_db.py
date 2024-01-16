import sqlite3

def create_database():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Create a table to store questions and choices
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT,
            choice1 TEXT,
            choice2 TEXT,
            choice3 TEXT,
            choice4 TEXT,
            correct_choice INTEGER
        )
    ''')

    # Insert sample data
    cursor.executemany('''
        INSERT INTO questions (question_text, choice1, choice2, choice3, choice4, correct_choice)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', [
        ("What is the basic unit of Life?", "Cell", "Organ", "Tissue", "System", 1),
        ("What is the process by which plants make food?", "Digestion", "Respiration", "Photosynthesis", "Reproduction", 3),
        ("Which of the following is NOT a living thing?","Plant", "Animal", " Rock", "Bacteria", 3),
        ("Which of the following is NOT a part of the plant cell?", "Cell wall", "Nucleus", " Mitochondria", "Chlorophyll", 4),
        ("What is the function of the heart?", "To pump blood", "To digest food", "To filter blood", "To protect the brain", 1),
        ("What is the largest organ in the human body?", "Skin", "Liver", "Brain", "Heart", 1),
        ("Which of the following is NOT a part of the digestive system?", "Mouth", "Stomach", "Intestines", "Lungs", 4),
        ("What is the function of the respiratory system?", "To bring oxygen into the body and remove carbon dioxide", "To digest food", "To pump blood", "To protect the brain", 1),
        ("What is the process by which animals reproduce?", "Sexual reproduction","Asexual reproduction", "Both A and B", "None of the above", 3),
        ("What is the difference between a herbivore and a carnivore?", "A herbivore eats plants, while a carnivore eats animals", "A herbivore is a producer, while a carnivore is a consumer", "A herbivore has a backbone, while a carnivore does not", "A herbivore is warm-blooded, while a carnivore is cold-blooded.", 1),


        # Add more questions here
    ])

    conn.commit()
    conn.close()
