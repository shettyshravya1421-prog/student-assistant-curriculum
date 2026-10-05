
course_notes = []
note_text = "A linked list is a data structure where each item points to the next one."
note_author = "Prof. Sharma"


note_numbers = [0.1, 0.9, 0.2, 0.05]

my_note = {
    "author": note_author,
    "text": note_text,
    "embedding": note_numbers
}
 
course_notes.append(my_note)
print("Note was saved")
print(my_note)