# 🚀 FastAPI Data Platform Lesson

A modern data ingestion pipeline built with **FastAPI** and **PostgreSQL**. This project demonstrates how to receive, validate, and store complex JSON data.

## 🛠️ Tech Stack
* **FastAPI**: For the web framework and API endpoints.
* **Pydantic**: For data validation and schema definitions.
* **PostgreSQL**: As the persistent storage using `JSONB` for flexibility.
* **Psycopg**: To manage the database connection pooling.

## 📋 Features
* **Nested Data**: Handles product dimensions (width, height, depth).
* **Tagging System**: Supports a list of tags for each product.
* **Automatic Validation**: Returns `422 Unprocessable Entity` if data format is incorrect.

## 🚀 How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Start server: `python3 -m uvicorn main:app --reload`
3. Access the data at `http://127.0.0.1:8000/products`
Updated feb 10
