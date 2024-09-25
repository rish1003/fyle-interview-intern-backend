

## Completed Tasks

- **Implemented Missing APIs**: Developed the missing APIs as outlined in the challenge requirements.
- **Grading API Tests**: Created comprehensive tests for the grading API to ensure its functionality.
- **Bug Fixes**: Resolved intentional bugs present in the application to ensure that all tests pass successfully.
- **Achieved Test Coverage**: Improved overall test coverage to exceed 94%.
- **Dockerized the Application**: Docker allows for consistent development and production environments, making it easier to manage dependencies and configurations. 

Below are the steps taken to Dockerize the application, along with the relevant changes made to the codebase.

## Installation

1. Fork this repository to your github account
2. Clone the forked repository and proceed with steps mentioned below

### Docker Setup
Install Docker Desktop (if not already installed)
To run the application using Docker, you can use the following commands:

1. **Build the Docker image:**
    ```bash
    docker0compose build
    ```

2. **Run the Docker container:**
    ```bash
    docker run -p 7755:7755 fyle-backend
    ```
3. **Go into docker bash**
    ```bash
    docker exec -it fyle-interview-intern-backend-fylein-app-1 bash
    ```

### Install requirements

```
virtualenv env --python=python3.8
source env/bin/activate
pip install -r requirements.txt
```

### Reset Database

To reset the database, follow these steps:

1. Set the Flask application environment variable:
    ```bash
    export FLASK_APP=core/server.py
    ```

2. Remove the existing database file:
    ```bash
    rm core/store.sqlite3
    ```

3. Run the database migrations:
    ```bash
    flask db upgrade -d core/migrations/
    ```

### Run Tests

To run the tests and generate a coverage report, use the following commands:

1. **Run all tests:**
    ```bash
    pytest -vvv -s tests/
    ```

2. **Run tests with coverage:**
    ```bash
    pytest --cov --cov-report html:htmlcov tests/ 

    ```

3. **Open the HTML coverage report:**
    Open htmcov/index.html on your browser.

## Test Coverage Reports

- Detailed coverage report can be accessed [here](coverage.html).
- Tests report can be accessed [here](tests.jpg)

## Conclusion

Thank you for offering this chance to work on this project. Looking forward to further steps.