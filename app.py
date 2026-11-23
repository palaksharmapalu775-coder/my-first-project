# Campus Saathi - AI Study Buddy for BCA Students
# Made by Palak - BCA Student

class CampusSaathi:
    def __init__(self):
        self.doubts = []

    def notes_summarizer(self):
        print("\n--- Notes Summarizer ---")
        notes = input("Apni lambi notes yaha paste karo:\n")
        sentences = notes.split('.')
        summary = '. '.join(sentences[:3])
        print("\n--- Tera Short Summary ---")
        print(summary + ".")
        print("\nTip: In 3 lines ko yaad kar lo, 80% topic cover ho jayega.")

    def quiz_maker(self):
        print("\n--- Auto Quiz Maker ---")
        print("Topic: Python OOP")
        questions = [
            ("Python me class banane ke liye kaunsa keyword use hota hai? \n a) class  b) def  c) object \n Jawab: ", "a"),
            ("OOP me data ko chhupane ko kya kehte hain? \n a) Inheritance  b) Encapsulation  c) Polymorphism \n Jawab: ", "b"),
            ("__init__ kya hai? \n a) Function  b) Constructor  c) Variable \n Jawab: ", "b")
        ]
        score = 0
        for q, ans in questions:
            user_ans = input(q).lower()
            if user_ans == ans:
                print("Sahi!")
                score += 1
            else:
                print(f"Galat, sahi jawab {ans} tha.")
        print(f"\nTera Score: {score}/3")

    def resume_checker(self):
        print("\n--- Resume Checker ---")
        resume = input("Apna resume ka text yaha paste karo:\n").lower()
        score = 0
        checks = {
            "python": "Python skill mili",
            "project": "Project section mila",
            "internship": "Internship mention hai",
            "linkedin": "LinkedIn link hai"
        }
        for word, msg in checks.items():
            if word in resume:
                print(f"OK {msg}")
                score += 25
            else:
                print(f"MISSING {msg} - Missing hai, add karo")
        print(f"\nTera Resume Score: {score}/100")

    def doubt_tracker(self):
        print("\n--- Doubt Tracker ---")
        doubt = input("Kis topic me doubt hai? Likho: ")
        self.doubts.append(doubt)
        print(f"Save ho gaya! Tere total doubts: {self.doubts}")

    def menu(self):
        while True:
            print("\n===== CAMPUS SAATHI =====")
            print("1. Notes Summarizer")
            print("2. Auto Quiz Maker")
            print("3. Resume Checker")
            print("4. Doubt Tracker")
            print("5. Exit")
            choice = input("Kya karna hai? (1-5): ")
            if choice == "1":
                self.notes_summarizer()
            elif choice == "2":
                self.quiz_maker()
            elif choice == "3":
                self.resume_checker()
            elif choice == "4":
                self.doubt_tracker()
            elif choice == "5":
                print("Bye! Padhai karte raho")
                break
            else:
                print("Galat number, 1 se 5 tak daalo.")

if __name__ == "__main__":
    app = CampusSaathi()
    app.menu()