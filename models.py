import json
import random

class Question:
    def __init__(self, qid, text, options, answer):
        self.qid = qid
        self.text = text
        self.options = options
        self.answer = answer

    def ask(self,number=None):
        if number:
            print(f"\nQ{number}: {self.text}")
        else:
            print(f"{self.qid}: {self.text}")

        for i, opt in enumerate(self.options):
            print(f"{chr(65+i)}){opt}")

        return input("Your answer (A/B/C/D): ").strip().upper()


        # ask question here
class Quiz:
    def __init__(self,file_path):
        self.questions_file = file_path
        self.questions = self.load_questions()


    def load_questions(self):
        with open(self.questions_file,"r") as f:
            data = json.load(f)
        return [Question(q["id"], q["question"], q["options"], q["answer"]) for q in data]

    def run(self,mistakes, notes, mode="full"):
        if mode == "mistake":
            data = mistakes.get_all()
            if not data:
                print("\n No mistakes to review!")
                return
            questions = [Question(m["id"], m["question"],m["options"], m["answer"]) for m in data]
        else:
            questions = self.questions
        random.shuffle(questions)
        score = 0
        for i, q in enumerate(questions, start=1):
            ans = q.ask(i)
            if ans == q.answer:
                print("Correct!")
                score+=1
                if mistakes.contains(q.qid):
                    remove = input("Remove from mistake list? (y/n): ").strip().lower()
                    if remove =="y":
                        mistakes.remove(q.id)
                        print("Removed from mistake list")
                    else:
                        print("kept in mistake list")
                else:
                    print(f" Wrong. Correct answer:{q.answer}")
                    mistakes.add(q)
                
                add_note = input("Would you like to add a note? (y/n): ").strip().lower()
                if add_note == "y":
                    note_text = input("Enter your note: ").strip()
                    notes.add(q.qid, q.text,note_text)
            print(f"\nQuiz finished! Score:{score}/{len(questions)}")

class MistakeList:
    def __init__(self,file_path):
        self.file_path = file_path
        self.mistakes = self.load()

    def load(self):
        try:
            with open(self.file_path,"r") as f:
                content = f.read().strip()
                if not content:
                    return []
                return json.loads(content)
        except FileNotFoundError:
            return []
    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.mistakes,f, indent=2)

    def add(self,question):
        if not any(m["id"] == question.qid for m in self.mistakes):
            self.mistakes.append({
                "id": question.qid,
                "question": question.text,
                "options": question.options,
                "answer": question.answer
            })
            self.save()

    def remove(self,qid):
        self.mistakes = [m for m in self.mistakes if m["id"] != qid]
        self.save()
    def contains(self,qid):
        return any(m["id"] == qid for m in self.mistakes)
    def get_all(self):
        return self.mistakes
    

        





class NoteManager:
    def __init__(self,file_path):
        self.file_path = file_path
        self.notes = self.load()
        
    def load(self):
        try:
            with open(self.file_path, "r") as f:
                content = f.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except FileNotFoundError:
            return {}
    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.notes, f, indent=2)

    def add(self, qid, question_text, note_text):
        qid = str(qid)

        if qid in self.notes:
            print(f"\n Existing notes for Q{qid}:")
            for i, old_note in enumerate(self.notes[qid]["notes"], start=1):
                print(f"    {i}.{old_note}")
            
            print("\nWhat would you like to do?")
            print("A) Append (keep old + add new)")
            print("B) Replace (overwrite old note)")
            print("C) No additional note")

            choice = input("Choose A/B/C: ").strip().upper()

            if choice =="A":
                self.notes[qid]["notes"].append(note_text)
                print("New note appended.")
            elif choice =="B":
                self.notes[qid]["notes"] = [note_text]
                print("Note replaced.")
            elif choice == "C":
                print("No new note added.")
            else:
                print("Invalid choice. Keeping old notes only.")
        else:
            self.notes[qid] = {
                "question": question_text,
                "notes": [note_text]
            }
            print("Node added")
        self.save()




    def view_all(self):
        if not self.notes:
            print("\n No notes yet.")
            return
        print("\n----Your notes----")
        for qid, data in self.notes.items():
            print(f"Q{qid}: {data['question']}")
            for i, note in enumerate(data["notes"], start=1):
                print(f"    {i}.{note}")