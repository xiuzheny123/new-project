from models import Quiz, MistakeList, NoteManager


def main():
    quiz = Quiz("qustions.json")
    mistakes = MistakeList("mistaks.json")
    notes = NoteManager("notes.json")

    while True:
        user_choice = input("Select:\n\t1 Take full Quiz \n\t2 Take Mistake Quiz\n\t3 View Notes\n\t4 Quit")
        if user_choice == "1":
            quiz()
        elif user_choice == "2":
            mistakes()
        elif user_choice == "3":
            notes()
        elif user_choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice, please try again")




if __name__ == "__main__":
    main()