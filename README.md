# Employee Management API

A robust, lightweight RESTful API built using Python, Django, and Django REST Framework (DRF) to handle employee directory records securely. This project demonstrates modular backend design, structured database schemas, data validation, and clean REST endpoints.

## 🚀 Features
* **Full CRUD Support:** Endpoints configured for creating, reading, updating, and deleting records.
* **Custom Data Schema:** Tracks key information including unique IDs, localized names, gender attributes, and contact records.
* **Built-in Validation:** Serializer layer enforces structured data formats (e.g., specific character lengths, email integrity).
* **Database Driven:** Integrated with SQLite for development efficiency.

---

## 🛠️ Tech Stack
* **Backend Framework:** Django 6.0.5
* **API Toolkit:** Django REST Framework (DRF)
* **Database:** SQLite
* **Environment:** Python 3.14 Virtual Environment (`venv`)

---

## ⚙️ Core Data Schema

| Field Name | Data Type | Constraints / Rules |
| :--- | :--- | :--- |
| `id` | Integer | Auto-incrementing Primary Key |
| `emp_id` | Character | Unique Identifier (max 20 chars) |
| `first_name` | Character | String (max 50 chars) |
| `last_name` | Character | String (max 50 chars) |
| `gender` | Character | Choices: `M` (Male), `F` (Female), `O` (Other) |
| `phone_number`| Character | Contact String (max 15 chars) |
| `email_id` | Email | Unique System-wide Email Field |

---

## 📡 API Endpoints

| HTTP Method | Endpoint URL | Action |
| :--- | :--- | :--- |
| **GET** | `/api/employees/` | Retrieve a list of all saved employee records |
| **POST** | `/api/employees/` | Create/Save a brand new employee entry |
| **GET** | `/api/employees/<id>/` | Fetch a specific employee record by their ID |
| **PUT** | `/api/employees/<id>/` | Update an existing employee's data fields |
| **DELETE**| `/api/employees/<id>/` | Permanently drop an employee record from the DB |

---

## 💻 Setup and Local Installation

Follow these quick commands to spin up the development engine on your local machine:

1. **Clone the repository and enter the directory:**
   ```bash
   cd employee-api
