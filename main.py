from models import Quiz, MistakeList, NoteManager
from exceptions import InvalidMenuChoice


def main():
    quiz = Quiz("questions.json")
    mistakes = MistakeList("mistakes.json")
    notes = NoteManager("notes.json")

    while True:
        try:
            user_choice = input("Select:\n\t1 Take full Quiz \n\t2 Take Mistake Quiz\n\t3 View Notes\n\t4 Quit\n")
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
                raise InvalidMenuChoice(f"{user_choice} is not a valid option, please choose 1-4")
        except InvalidMenuChoice as e:
            print(f"Error:{e}")




if __name__ == "__main__":
    main()