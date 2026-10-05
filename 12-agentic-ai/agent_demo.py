# step 1: make a function that answers using saved notes
def search_notes():
    return "A linked list connects items using pointers."

# step 2: make a function that does math
def get_average(a, b, c):
    return (a + b + c) / 3

# step 3: make the agent decide what to do
student_question = "What is my average GPA?"

if "average" in student_question:
    print("Using the calculator tool")
    result = get_average(8.5, 9.0, 7.8)
    print("Your average is:", result)
else:
    print("Using the search tool")
    result = search_notes()
    print(result)