# Overengineered for the assignment, don't copy but feel free to look and ask.
class Question:
    def __init__(self, question, value_type):
        self.__question = question
        self.__value_type = value_type
        self.__answer = None
    
    def get_question(self):
        return self.__question
    
    def get_answer(self):
        return self.__answer
    
    # Will return true if it was a valid answer, false if not
    def set_answer(self, new_answer):
        try:
            if isinstance(new_answer, self.__value_type):
                self.__answer = new_answer
                return True
        except Exception:
            return False

questions = [
    Question("What is your name: ", str),
    Question("What is your age: ", int),
    Question("What is your favourite color: ", str),
    Question("How many hours have you been awake: ", int),
    Question("Do you smoke or vape: (True/False) ", bool)
]

def ask_questions():
    for question in questions:
        answer = None
        while answer is None or not question.set_answer(answer):
            try:
                raw_input = input(question.get_question())
                # Convert raw input to the expected type
                if question._Question__value_type == int:
                    answer = int(raw_input)
                elif question._Question__value_type == bool:
                    answer = bool(raw_input)
                elif question._Question__value_type == str:
                    answer = raw_input
                else:
                    answer = None # Default to None for unsupported types
            except ValueError:
                answer = None # Reset answer if there's a conversion error

def print_questions():
    for question in questions:
        print(question.get_answer())

ask_questions()
print_questions()
