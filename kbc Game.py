def start_quiz():
    # Welcome message
    print("!! WELCOME TO KBC !!")
    print("Answer the following questions to win prize money!")

    # Define the questions, choices, and correct answers
    questions = [
        {
            "question": "What does not grow on a tree according to a popular Hindi saying?",
            "choices": {
                "a": "Money",
                "b": "Flower",
                "c": "Leaves",
                "d": "Fruits"
            },
            "correct_answer": "a",
            "prize_money": 1000
        },
        # Add more questions here if needed
    ]

    prize_money = 0

    # Loop through the questions
    for q in questions:
        print("\n" + q["question"])
        for key, value in q["choices"].items():
            print(f"[{key}: {value}]")
        
        # Accept user input
        user_answer = input("Enter your answer: ").lower()
        
        # Check if the answer is correct
        if user_answer == q["correct_answer"]:
            print(f"Correct Answer! Your Prize Money is: ₹{q['prize_money']}")
            prize_money += q["prize_money"]
        else:
            print(f"Wrong Answer! The correct answer was '{q['correct_answer']}'.")
    
    # Display the total prize money
    print("\nQuiz Over!")
    print(f"Your Total Prize Money is: ₹{prize_money}")

# Start the quiz
if __name__ == "__main__":
    start_quiz()