   # my python quiz project
    


questions = ("How many department you find in Haiti?: ",
              "what's Haiti's Capital?: ", 
              "what's Haiti independance date?: ", 
              "where you find Hinche?: ")

Options = ( ("A. 11", "B. 9", "C. 12", "D. 10"),
            ("A. Cap-Haitien", "B. Cayes", "C. Port-au-prince", "D. Jacmel"),
            ("A. 1803", "B. 1704", "C. 1804", "D. 1904"),
            ("A. USA","B. Tayiti", "C. Dominican Republique", "D. Haiti"))

answers = ("D", "C", "c", "D")
guesses = []
score = 0
question_num = 0
for question in questions:
        print("------------------------------------------")
        print(question)
        for option in Options[question_num]:
            print(option)
        guess = input("choose_a_letter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("correct!")
        else:
            print("incorrect!")
            print(f"{answers[question_num]} the true answer")
        question_num += 1
print("----------------------------")
print("           result          ")
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
print(f"your score is: {score}%")
