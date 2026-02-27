import time
import random

sentences = [

"Python is a powerful programming language",

"I am learning python programming",

"Computer science is very interesting",

"Practice coding everyday to improve skills",

"Programming makes problem solving easy"

]

print("===== Typing Speed Tester =====\n")

sentence=random.choice(sentences)

print("Type this sentence:\n")

print(sentence)

input("\nPress Enter to Start...")

start=time.time()

typed=input("\nStart Typing:\n")

end=time.time()

time_taken=end-start

words=len(typed.split())

wpm=words/(time_taken/60)

correct=0

for i in range(min(len(sentence),len(typed))):

    if sentence[i]==typed[i]:

        correct+=1

accuracy=(correct/len(sentence))*100

print("\nResult")

print("Time Taken:",round(time_taken,2),"seconds")

print("Typing Speed:",round(wpm,2),"WPM")

print("Accuracy:",round(accuracy,2),"%")