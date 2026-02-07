# List of questions
questions = [
    "Which planet is known as the Red Planet?",
    "Who wrote the national anthem of India?",
    "What is the capital of France?",
    "Which gas do plants absorb from the atmosphere?"
]

# List of options
options = [
    ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
    ["1. Rabindranath Tagore", "2. Mahatma Gandhi", "3. Iqbal", "4. Subhash Chandra Bose"],
    ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"],
    ["1. Nitrogen", "2. Oxygen", "3. Carbon Dioxide", "4. Hydrogen"]
]

# Correct answers (store index of correct option)
answers = [2, 1, 3, 3]  # 1-based indexing

# Prize money for each correct answer
prize_money = [1000, 2000, 3000, 5000]

total_amount = 0

print("🎉 Welcome to Mini KBC! 🎉\n")

for i in range(len(questions)):
    print(f"Q{i+1}: {questions[i]}")
    for opt in options[i]:
        print(opt)

    user_ans = int(input("Enter your answer (1-4): "))

    if user_ans == answers[i]:
        print("✔ Correct Answer!")
        total_amount += prize_money[i]
    else:
        print("❌ Wrong Answer!")
        break

    print()

print(f"\n💰 Total amount you take home: ₹{total_amount}")
print("Thank you for playing! 🙌")