from models import Quiz, MistakeList, NoteManager


def main():
    quiz = Quiz("questions.json")
    mistakes = MistakeList("mistakes.json")
    notes = NoteManager("notes.json")

    while True:
        user_choice = input("Select:\n\t1 Take full Quiz \n\t2 Take Mistake Quiz\n\t3 View Notes\n\t4 Quit")
        if user_choice == "1":
            quiz.run(mistakes,notes, mode="full")
        elif user_choice == "2":
            quiz.run(mistakes, notes,mode="mistake")
        elif user_choice == "3":
            notes.view_all()
        elif user_choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again")




if __name__ == "__main__":
    main()