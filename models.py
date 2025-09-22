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
        self.questions = self.load()


    def load_questions(self):
        with open(self.questions_file,"r") as f:
            data = json.load(f)
        return [Question(q["id"]), q["question"], q["options"], q["answer"] for q in data]

    def run(self ):
        pass


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
        
