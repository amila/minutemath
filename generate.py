import random
import os
import sys
import time
import threading

total_questions = 20
time_duration = 1000*60

top_minimum=0
top_maximum=20

bottom_minimum=1
bottom_maximum=20

repeat_incorrect_question=False





bad_colour = '\033[1;31;40m '
good_colour = '\x1b[1,255,0m '

correct_answers = 0
incorrect_questions = []
correct_questions = []
start_time = time.time()

def create_questions(number_of_questions=10, top_min=11,top_max=20,bottom_min=0, bottom_max=9, max_result=9, min_result=0):
    questions = []
    if max_result is None:
        max_result = 99999
    
    if min_result is None:
        min_result = -99999
    
    answer_range = range(min_result, max_result)

    while(len(questions) < number_of_questions):
        top_number = random.randint(top_min,top_max)
        bottom_number = random.randint(bottom_min, bottom_max)

        if (top_number-bottom_number) in answer_range:
            questions.append((top_number, bottom_number))

    
    return questions

def timeout(seconds=1*60):

    time.sleep(time_duration)
    print_results(True)

    os._exit(0)

def format_subtraction_question(question, colour='\x1b[1;255;40m '):
    result = colour + str(question[0]) + '-' + str(question[1]) + ' = '
    if len(question) == 3:
        result = result + question[2]
    return result


def print_results(timeout=False):
    now = time.time()
    os.system("clear")
    print("===========================================================================================")
    if timeout:
        print("Time is up!!!")
    
    print("You got " + str(correct_answers) + " correct out of " + str(total_questions) + " questions!")
    print("It took you " + str((now-start_time)/60) + "minutes to complete.")
    
    if len(incorrect_questions) == 0:
        print("Great work! All the questions you answered were correct!!!")

    print("These are the questions you got correct:")
    for question in correct_questions:
        print(format_subtraction_question(question))
    print("These are the questions you got incorrect:")
    for question in incorrect_questions:
        print(format_subtraction_question(question, colour=bad_colour))
    print("===========================================================================================")
    print("")
    print("")

if __name__ == "__main__":
    questions = create_questions(number_of_questions= total_questions, top_min=top_minimum, top_max=top_maximum, bottom_min=bottom_minimum, bottom_max=bottom_maximum)

    question_counter = 0
    streak = 0
    
    t = threading.Thread(target=timeout)
    t.start()
    for question in questions:
        correct_answer= False
        points_per_question = 1
        question_counter = question_counter + 1
        question_answered = False

        while( (repeat_incorrect_question and not correct_answer) or not question_answered):
            os.system("clear")
            print("You got " + str(streak) + " questions correct in a row!")

            val = input('#' + str(question_counter) + '. ' + format_subtraction_question(question, colour=good_colour))
            
            if not val.isnumeric():
                os.system("clear")
                continue

            question_answered = True
            correct_answer = question[0]-question[1] == int(val)

            if correct_answer:
                streak = streak + 1
                correct_answers = correct_answers + 1
                correct_questions.append((question[0],question[1],val))
            else:
                points_per_question = 0
                incorrect_questions.append((question[0],question[1],val))
                streak = 0
            

            


    print_results(False)
    os._exit(0)
    
        
    
