# 📚 FastAPI Book Manager API

A high-performance RESTful API built with **FastAPI** for managing a book inventory. This project demonstrates full **CRUD (Create, Read, Update, Delete)** operations, database integration using **SQLAlchemy ORM**, and data validation with **Pydantic**. 

## ⚙️ Key Technologies Used

* **FastAPI:** Modern, fast (high-performance) web framework for building APIs.
* **Python:** The core programming language.
* **SQLAlchemy:** Python SQL Toolkit and Object-Relational Mapper (ORM).
* **MySQL:** Persistent SQL database for data storage.
* **Pydantic:** Used for data validation and schema definition.

## 🌟 Features

* **CRUD Operations:** Fully functional endpoints for adding, viewing, updating, and deleting books.
* **Database Session Management:** Utilizes FastAPI's Dependency Injection (`get_db`) for efficient and safe database connections.
* **Automatic Documentation:** API documentation (Swagger UI) is automatically generated at `/docs`.
* **Data Models:** Clear separation of Pydantic schemas (`schemas.py`) and SQLAlchemy ORM models (`model.py`).

## 📌 API Endpoints

| Method | Endpoint | Description | Pydantic Schema |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Root endpoint confirmation. | - |
| `GET` | `/books` | Retrieve a list of all books. | `model.book` |
| `GET` | `/book/{book_id}` | Retrieve a specific book by ID. | `model.book` |
| `POST` | `/book` | **Create** a new book entry. | `schemas.add_book` |
| `PUT` | `/book/{book_id}` | **Update** an existing book's details. | `schemas.update_book` |
| `DELETE` | `/book/{book_id}` | **Delete** a book by ID. | - |

## 🛠️ Local Setup

Follow these steps to set up and run the FastAPI Book Manager API locally.

### 1. Database Setup (MySQL)

You need an instance of a MySQL server running to connect to.

1.  **Create Database:** Create a MySQL database named `book_manager`.
2.  **Create User:** Create a dedicated MySQL user (e.g., `bookuser`) with a strong password and grant it permissions on the `book_manager` database.
3.  **Update Connection String:** Edit the `database_url` in **`database.py`** to match your credentials:
    ```python
    # database.py
    database_url = "mysql+mysqlconnector://bookuser:Roshaan_DB2024!@localhost:3306/book_manager" 
    ```

### 2. Environment Setup & Dependencies

It is highly recommended to use a virtual environment (`venv`) to isolate project dependencies.

1.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

2.  **Activate the Environment:**
    * **Windows (Command Prompt/Git Bash):**
        ```bash
        ./venv/Scripts/activate
        ```
    * **(Linux/macOS):**
        ```bash
        source venv/bin/activate
        ```
    *(Your terminal prompt should now show `(venv)` to indicate activation.)*

3.  **Install Dependencies:** Install all necessary libraries and their exact versions using the provided `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Run the API

1.  **Start the Uvicorn Server:**
    ```bash
    uvicorn main:app --reload
    ```
    
2.  The API will be running at `http://127.0.0.1:8000`. You can test all endpoints and view the documentation using the interactive Swagger UI at `http://127.0.0.1:8000/docs`.
