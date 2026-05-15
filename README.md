# Python CRUD Application using SQLAlchemy & MySQL

A simple CRUD (Create, Read, Update, Delete) application built using Python, SQLAlchemy ORM, and MySQL.

## Features

- Add users
- Get all users
- Update user details
- Delete users
- Prevent duplicate users
- Database session management
- Environment variable configuration using dotenv

## Technologies Used

- Python
- SQLAlchemy
- MySQL
- PyMySQL
- python-dotenv

## Project Structure

```text
project/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/sindhurametla/your-repository-name.git
cd your-repository-name
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file and add:

```env
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=your_database_name
```

## Run Application

```bash
python main.py
```

## Available Operations

- add
- update
- getusers
- delete

## Example

```text
Enter your choice(add/update/getusers/delete): add
Enter your name: John
Enter your age: 25
User added successfully
```

## Learning Outcomes

- SQLAlchemy ORM basics
- CRUD operations in Python
- Database model creation
- MySQL integration
- Session management
- Using environment variables securely

## Author

Sindhura Metla

GitHub: https://github.com/sindhurametla/sqlalchemycrud.git
