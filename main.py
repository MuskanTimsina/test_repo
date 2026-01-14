from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

class student(BaseModel):
    id:int
    name:str
    age:int
    faculty:str

class student_patch(BaseModel):
    id:Optional[int]=None
    name:Optional[str]=None
    age:Optional[int]=None
    faculty:Optional[str]=None 

students=[]

# HTTP get request with the ID valdation
@app.get("/students/{student_id}")
def get_student(student_id:int):
    for s in students:
        if s.id==student_id:
            return{"message":"students management system","student":s}
        # actual ID validation is here.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"student with this id:{student_id} is not found") 

# HTTP post reques with the ID validation.
@app.post("/students")
def create_student(new_students:student):
    # actual ID validation here.
    for s in students:
        if s.id==new_students.id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="The student with tihis id is already exist")
    students.append(new_students)
    return{"message":"student is successfully added!",
           "student":new_students}

# HTTP update request with the ID validation.
@app.put("/students/{student_id}")
def update_student(student_id:int,updated_student:student):
    for index,s in enumerate(students):
        if s.id==student_id:
            updated_student.id=student_id
            students[index]=updated_student
            return{"message":f"student with this id:{student_id}is updated sucessfully",
                   "student":updated_student}
            # actual ID validation here.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"student with this {student_id}is not available")  
      
# HTTP delete request with ID validation .
@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for index,s in enumerate(students):
        if s.id==student_id:
            students.pop(index)
            return{"message":"student is deleted successfully"}
        # actual ID validation is here.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"student with this id:{student_id}is not found")

# HTTP patch request with ID validation here.
@app.patch("/students/{student_id}")
def students_patch(student_id:int,studentpatch:student_patch):
    for index,s in enumerate(students):
        if s.id==student_id:
            if studentpatch.name is not None:
                s.name=studentpatch.name
            if studentpatch.age is not None:
                s.age=studentpatch.age
            if studentpatch.faculty is not None:
                s.faculty=studentpatch.faculty
            student[index]=s
            #actual ID validation is here.
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"student with the id:{student_id},is not found.")        

    