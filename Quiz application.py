

# QUIZ APPLICATION



questions = {
    "What is the capital of INDIA?": "Delhi",
    "What is 2 + 2?": "4",
    "What is the capital of uttar pradesh?": "Lucknow",
    "What is best internship app?": "Internshala",
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {answer}.")

print(f"Your final score is {score}/{len(questions)}.")

