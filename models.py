import json
import random

class Question:
    def __init__(self, qid, text, options, answer):
        self.qid = qid
        self.text = text
        self.options = options
        self.answer = answer

    def ask(self,number=None):
        pass

        # ask question here
class Quiz:
    def __init__(self,file_path):
        self.questions_file = file_path
        self.questions = self.load()
class MistakeList:
    def __init__(self,file_path):
        self.file_path = file_path
        self.mistakes = self.load()
class NoteManager:
    def __init__(self,file_path):
        self.file_path = file_path
        self.notes = self.load()
        
