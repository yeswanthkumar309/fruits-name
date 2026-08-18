# API-Based CRUD Web Application

A full-stack web application that uses REST APIs to manage data dynamically. Users can **add, view, update, and delete data** through the application.

## Features

* Add new data
* View existing data
* Update data
* Delete data
* REST API integration
* Interactive frontend

## Technologies Used

* HTML
* CSS
* JavaScript
* FastAPI
* REST API

## How It Works

The frontend sends API requests to the FastAPI backend.

```text
Frontend
   ↓
REST API
   ↓
FastAPI Backend
   ↓
Data
```

### API Operations

| Method | Purpose     |
| ------ | ----------- |
| GET    | View data   |
| POST   | Add data    |
| PUT    | Update data |
| DELETE | Delete data |

## Running the Project

Start the FastAPI backend:

```bash
fastapi dev main.py
```

The API will be available locally at:

```text
http://127.0.0.1:8000
```

Open the frontend in your browser to use the application.

## License

This project is licensed under the MIT License.
