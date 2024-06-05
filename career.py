# Career options
career_options = ["Software Engineer", "Doctor", "Teacher", "Graphic Designer","electrical Engineer","civil engineerin"]

# Career advices
career_advices = {
    "Software Engineer": "You should have a strong interest in problem-solving and programming languages.",
    "Doctor": "You need to have a passion for helping others and be willing to undergo extensive medical training.",
    "Teacher": "Patience, communication skills, and a love for education are essential for this career.",
    "Graphic Designer": "Creativity and proficiency in design software are key for success in this field."
}

# Career questions
career_questions = [
    "Do you enjoy solving complex problems?",
    "Are you interested in the medical field?",
    "Do you like working with children or young adults?",
    "Are you passionate about visual arts and design?"
]

# Function to get user input and determine career choice
def determine_career():
    print("Welcome to the Career Recommendation Program!")
    print("Answer the following questions to discover your ideal career.")

    user_answers = []
    for question in career_questions:
        answer = input(question + " (yes/no): ").lower()
        while answer not in ["yes", "no"]:
            print("Please enter 'yes' or 'no'.")
            answer = input(question + " (yes/no): ").lower()
        user_answers.append(answer)

    for index, answer in enumerate(user_answers):
        if answer == "yes":
            print("Based on your answers, you might enjoy becoming a", career_options[index])
            print("Advice:", career_advices[career_options[index]])
            return
    print("Sorry, we couldn't determine a suitable career based on your answers.")

# Call the function to run the program
determine_career()