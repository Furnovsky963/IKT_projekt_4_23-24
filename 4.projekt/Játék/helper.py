import random
from time import sleep
from os import system as s
from termcolor import colored

def write(user_input: str, colors: str) -> None:
    try:
        user_input = colored(user_input, colors)
    except:
        colors = "light_grey"
        user_input = colored(user_input, colors)
    
    finally:
        for i in user_input:
            if i != " ":
                count = random.randint(3, 13)
                count = count/75
                print(i, end="",flush=True)
                sleep(count)
                
            elif i == " ":
                count = random.randint(3, 11)
                count = count/20
                print(i, end="",flush=True)
                sleep(count)
       
def cl():
    s("cls")
    
def qna(x):
    a = []
    if x == 1:
        a = ["0","4","8","12","16"]
    
    elif x == 2:
        a = ["20","24","28","32","36"]
    
    elif x == 3:
        a = ["40","44","48","52","56"]
        
    elif x == 4:
        a = ["60","64","68","72","76"]
        
    elif x == 5:
        a = ["80","84","88","92","96"]

    get_q = random.choice(a)
    get_q = int(get_q)
    
    get_a = 0
    get_wrong_a1 = 0
    get_wrong_a2 = 0

    get_a += get_q + 1
    get_wrong_a1 += get_q + 2
    get_wrong_a2 += get_q + 3
    
    
    question = []
    answer = []
    wrong_answer_1 = []
    wrong_answer_2 = []

    all = []
    
    with open("kerdesek.txt", "r", encoding="utf-8") as file:
        for line in file:
            all.append(line)

    question.append(all[get_q])
    answer.append(all[get_a])
    wrong_answer_1.append(all[get_wrong_a1])
    wrong_answer_2.append(all[get_wrong_a2])
    
    #print(f"{question} - Answer --> {answer}")

    finale_question = ""
    finale_answer = ""
    finale_w_answer1 = ""
    finale_w_answer2 = ""
    
    for i in question:
        finale_question += i
        
    for i in answer:
        finale_answer += i
        
    for i in wrong_answer_1:
        finale_w_answer1 += i
        
    for i in wrong_answer_2:
        finale_w_answer2 += i
        
    return finale_question, finale_answer, finale_w_answer1, finale_w_answer2
    #print(f"{finale_question}{finale_answer}")

#kerdes, valasz = qna(1)
#print(f"{kerdes}{valasz}")
 
#kerdes, valasz = qna(2)
#print(f"{kerdes}{valasz}")
if __name__ == "__main__":
    write("Almas pite","red")