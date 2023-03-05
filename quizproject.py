   # my python quiz project
    


questions = (" Konbyen depatman Ayiti genyen?: ",
              "Ki kapital Ayiti?: ", 
              "Nan ki ane Ayiti te pran endepandans: ", 
              "NAn ki peyi wap jwenn Ench: ")

Options = ( ("A. 11", "B. 9", "C. 12", "D. 10"),
            ("A. Okap", "B. Okay", "C. Potoprens", "D. Jakmel"),
            ("A. 1803", "B. 1704", "C. 1804", "D. 1904"),
            ("A. USA","B. Tayiti", "C. Sendomeng", "D. Ayiti"))

answers = ("D", "C", "c", "D")
guesses = []
score = 0
question_num = 0
for question in questions:
        print("------------------------------------------")
        print(question)
        for option in Options[question_num]:
            print(option)
        guess = input("antre (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("korek!")
        else:
            print("enkorek!")
            print(f"{answers[question_num]} se bon repons lan")
        question_num += 1
print("----------------------------")
print("           Rezilta          ")
print("----------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
    print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
    print()
score = (score / len(question) * 100)
print(f"sko w la se: {score}%")
