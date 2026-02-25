from fastapi import APIRouter, HTTPException
from models import Student
from database import get_connection

router = APIRouter()

@router.get("/students")
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM students"
    results = cursor.execute(sql).fetchall()
    conn.close()
    return {"students": results, "count": len(results)}

@router.get("/students/by-major")
def get_students_by_major(major: str):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "SELECT * FROM students WHERE (major = ?)"
    results = cursor.execute(sql, (major,)).fetchall()
    conn.close()
    return {"students": results, "count": len(results), "major": major}

@router.get("/students/by-gpa")
def get_students_by_gpa(min_gpa: float):
    if min_gpa >= 0.0 and min_gpa <= 4.0:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "SELECT * FROM students WHERE gpa = ?"
        results = cursor.execute(sql, (min_gpa,)).fetchall()
        conn.close()
        return {"students": results, "count": len(results), "min_gpa": min_gpa}
    else:
        raise HTTPException(status_code=400, detail="GPA must be between 0.0 and 4.0")


@router.get("/students/{student_id}", status_code=200)
def get_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT * FROM students WHERE id = ?"
    validation = cursor.execute(sql, (student_id,)).fetchone()

    if validation is None:
        raise HTTPException(status_code=404, detail="Student with ID" + student_id + " not found")
    
    conn.close()
    return validation


@router.post("/students", status_code=201)
def create_student(student: Student):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO students (name, email, major, gpa, enrollment_year) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(sql, (student.name, student.email, student.major, student.gpa, student.enrollment_year))
    conn.commit()
    id = cursor.lastrowid
    result = cursor.execute("SELECT * FROM students WHERE id = ?", (id,)).fetchone()
    conn.close()
    return result


@router.put("/students/{student_id}", status_code=200)
def update_student(student_id: int, student: Student):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        UPDATE students 
        SET (name, email, major, gpa, enrollment_year) 
            = (?, ?, ?, ?, ?) 
        WHERE id = ?"""
    cursor.execute(sql, (student.name, student.email, student.major, student.gpa, student.enrollment_year, student_id))

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail= "Student with ID " + student_id + " not found")

    result = cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()
    conn.commit()
    conn.close()

    return result
    #return {"id": result.id, "name": result.name, "email": result.email, "major": result.major, "gpa": result.gpa, "enrollment_year": result.enrollment_year}

@router.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM students WHERE id = ?"
    cursor.execute(sql, (student_id,))
    if cursor.rowcount <= 0:
        raise HTTPException(status_code=404, detail= f"Student with ID {student_id} not found")
    conn.commit()
    conn.close()
    return {"message" : "Student deleted successfully"}
