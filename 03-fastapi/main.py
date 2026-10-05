from fastapi import FastAPI
    
app = FastAPI()
    
@app.get("/")
def say_hello():
    return {"message": "Hello, this is the student API"}
    
@app.get("/student")
def get_student():
    student_name = "Sample Student"
    student_gpa = 8.7
    return {"name": student_name, "gpa": student_gpa}