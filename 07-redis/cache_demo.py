import redis
import time

r = redis.Redis(
    host="feeling-chartreuseish-trim-89333.db.redis.io",
    port=11340,
    password="LDn4etwXWHcT6rEKtQ7dUX3Cfb2pxzNP",
    decode_responses=True
)

def slow_lookup():
    print("Looking in the slow database...")
    time.sleep(2)
    return "Student GPA is 8.7"


saved_answer = r.get("student_gpa")

if saved_answer:
    print("Found in cache:")
    print(saved_answer)
else:
    print("Not in cache, checking the database")
    answer = slow_lookup()
    r.setex("student_gpa", 30, answer)
    print(answer)