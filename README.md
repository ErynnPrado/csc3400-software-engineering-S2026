# Student Records API

## Overview
The program is a RESTful API that utilizes SQLite and FastAPI. It uses CRUD operations to manage student records in a database.
Included are:
- 7 API endpoints (5 CRUD and 2 filtering)
- SQL queries (INSERT, SELECT, UPDATE, DELETE)
- Input validation using explicit checks and HTTPException
- Proper HTTP status codes (200, 201, 400, 401)

## Installation

### Prerequisites
1. Clone the repository using:
```sh
git clone "https://github.com/ErynnPrado/csc3400-software-engineering-S2026.git"
```
2. Create a virtual environment, then activate it:
```sh
python -m venv .venv
source .venv/Scripts/activate
```
3. Install dependencies from `requirements.txt`:
```sh
pip install -r requirements.txt
```
- You can verify installation via: `pip list | grep fastapi` & `uvicorn --version`

### Starting the server
4. Run:
```sh
uvicorn main:app --reload
```
5. `CTRL + Click` on the link provided in your terminal `http://localhost:8000`, this opens a new webpage in your browser.
- You can add `/docs` to the end of the URL to use FastAPI's user-friendly UI page.

## API Endpoints

### Get All Students
- **HTTP Method:** `GET`
- **URL Path:** `/students`
- **Description:** Retrives all student records.
- **Status Codes:**
    - `200` - Successful Response
---
### Get Student
- **HTTP Method:** `GET`
- **URL Path:** `/students/{student_id}`
- **Description:** Retrives a specific student by their ID.
- **Status Codes:**
    - `200` - Successful Response
    - `404` - Not Found
    - `422` - Validation Error
---
### Get Student By GPA
- **HTTP Method:** `GET`
- **URL Path**: `/students/by-gpa`
- **Description:** Retrive students with a GPA above a specified threshold.
    - Must be between $0.0$ and $4.0$.
- **Status Codes:**
    - `200` - Successful Response
    - `400` - Bad Request
    - `422` - Validation Error
---
### Get Students By Major
- **HTTP Method:** `GET`
- **URL Path:** `/students/by-major`
- **Description:** Retrives students filtered by their major.
- **Status Codes:**
    - `200` - Successful Response
    - `422` - Validation Error
---
### Create Student
- **HTTP Method:** `POST`
- **URL Path:** `/students`
- **Description:** Creates a new student record.
- **Status Codes:**
    - `201` - Successful Response
    - `422` - Validation Error
 ---
### Update Student
- **HTTP Method:** `PUT`
- **URL Path:** `/students/{student_id}`
- **Description: **
- **Status Codes:**
    - `201` - Successful Response
    - `422` - Validation Error
---
 ### Delete Student
- **HTTP Method:** `DELETE`
- **URL Path:** `/students/{student_id}`
- **Description:** Deletes a student record.
- **Status Codes:**
    - `200` - Successful Response
    - `404` - Not Found
    - `422` - Validation Error

## Testing
To test API calls, the easiest way is with FastAPI's `/docs` interface.

Once on the `/docs` page, click on any of the listed endpoints under the `default` section to expand it. Click the `Try it out` button at the top to test it, then enter in the required parameters (if any) and click `Execute`. Your API call will be executed and any information about it will be displayed below, as well as in the terminal.

### Note about database initialization
> The database is automatically initialized in `main.py`, which creates a `.db` file that stores any data you modify while testing. When you call one of the endpoints, they'll automatically connect to the this database file and commit any changes made.

## Example Usage

### `GET` - Student Record
**Request URL:** `http://127.0.0.1:8000/students/6`

**Response:** `200 OK`
```sh
{
  "id": 6,
  "name": "Carol White",
  "email": "carol.white@university.edu",
  "major": "Physics",
  "gpa": 3.9,
  "enrollment_year": 2023
}
```
---
### `POST` - Create a Student Record
**Request URL:** `http://127.0.0.1:8000/students/5`

**Request Body:**
```sh
{
  "name": "Shelby Mendez",
  "email": "smendez@example.edu",
  "major": "Biology",
  "gpa": 3.55,
  "enrollment_year": 2026
}
```

**Response:** `201 Created`
```sh
{
  "id": 5,
  "name": "Shelby Mendez",
  "email": "smendez@example.edu",
  "major": "Biology",
  "gpa": 3.55,
  "enrollment_year": 2026
}
```
---
### `GET` - By Major
**Request URL:** `http://127.0.0.1:8000/students/by-major?major=Biology`

**Request Body:** `GET /students/by-major?major=Biology`

**Response:** `200 OK`
```sh
{
  "students": [
    {
      "id": 5,
      "name": "Shelby Mendez",
      "email": "smendez@example.edu",
      "major": "Biology",
      "gpa": 3.55,
      "enrollment_year": 2026
    }
  ],
  "count": 1,
  "major": "Biology"
}
```
