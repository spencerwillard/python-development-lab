# Fraud Analysis — Python & PostgreSQL

## Project Overview

This mini-project explores how Python, PostgreSQL, and common development tools work together in a remote Linux environment.

The primary objective was to build a working development environment, connect Python to a PostgreSQL database, import a CSV dataset, and retrieve database records into a Pandas DataFrame.

The project emphasizes technical infrastructure, database connectivity, dependency management, and version control rather than advanced fraud analytics.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| PostgreSQL | Relational database for storing application records |
| Psycopg | Connects Python to PostgreSQL and executes SQL queries |
| Pandas | Converts query results into DataFrames |
| uv | Manages Python dependencies and the virtual environment |
| python-dotenv | Loads environment variables from a `.env` file |
| Git & GitHub | Version control and remote repository hosting |
| DigitalOcean | Hosts the Ubuntu Linux virtual machine |
| SSH & SCP | Remote access and secure file transfers |
| VS Code | Remote development environment |

## Project Workflow

The project follows this data flow:

```text
Local Mac
    |
    | SCP (secure file transfer)
    v
DigitalOcean Virtual Machine
    |
    | CSV Import
    v
PostgreSQL Database
    |
    | SQL Query via Psycopg
    v
Python Application
    |
    | DataFrame Creation
    v
Pandas
```

## Project Structure

```text
fraud-analysis/
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
├── uv.lock
└── src/
    └── fraud_analysis/
        └── __init__.py
```

The local `.env` file and source CSV are excluded from Git tracking.

## Database

The PostgreSQL database contains an `applications` table with 10,000 records imported from a CSV file.

### Table Schema

```sql
CREATE TABLE applications (
    application_id INTEGER PRIMARY KEY,
    application_date TIMESTAMP,
    identity_risk_score INTEGER
);
```

The table stores application identifiers, timestamps, and identity risk scores.

## Python Database Connection

The Python application uses Psycopg to connect to PostgreSQL and execute SQL queries.

Database credentials are stored in a local `.env` file rather than hardcoded into the application.

Example configuration:

```dotenv
DB_HOST=localhost
DB_NAME=learning_db
DB_USER=learning_user
DB_PASSWORD=your_password
```

The application loads these values using `python-dotenv` and retrieves them through Python's `os` module.

## Running the Project

**1. Install dependencies**

From the project directory:

```bash
uv sync
```

**2. Configure environment variables**

Create a `.env` file in the project root with the PostgreSQL connection details shown above.

**3. Prepare the database**

Create the `applications` table using the schema provided above, then import the source CSV into PostgreSQL.

**4. Execute the application**

```bash
uv run fraud-analysis
```

The application connects to PostgreSQL, retrieves the application records, creates a Pandas DataFrame, and calculates a simple risk-threshold review rate.

## Key Learning Outcomes

- Configured a remote Ubuntu Linux development environment.
- Used SSH to