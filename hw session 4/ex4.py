print("PLEASE ANSWER THESE ALGEBRAIC QUESTIONS")
choices = {
    "a" :[35, "about 55"],
    "b" :[36, "about 65"],
    "c" :[40, "about 75"],
    "d" :[44, "about 85"],
}

correct_ans = ["d","b"]

questions = ["If x=8, what is the value of 4(x+3) ? ",
"Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? "]

score = 0

for i in range(len(questions)):
    print(questions[i])
    for k, v in choices.items():
        print (k, v[i], sep=". ")
    user_choices = input("your choice: ").lower()
    if user_choices == correct_ans[i]:
        print("BINGO!")
        score += 1
    else:
        print("ehh")
print("YOU ANSWER CORRECTLY",score,"OUT OF",len(questions),"QUESTIONS!")
print()