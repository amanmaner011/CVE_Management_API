
# CVE Management API

This is a Flask-based application for managing a database of CVEs (Common Vulnerabilities and Exposures). The application allows users to add, retrieve, update, and delete CVE entries.


## Table of Contents

- [Features](#features)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Setup and Running the Application](#setup-and-running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing with Postman](#testing-with-postman)


## Features

- Add new CVEs
- Retrieve a specific CVE by its ID
- Retrieve all CVEs
- Update a CVE
- Delete a CVE


## Dependencies

- Python 3.9+
- Flask
- Flask-SQLAlchemy
- pandas


## Installation

1. Clone the Repository:
```bash
  git clone https://github.com/amanmaner011/CVE_Management_API.git
  cd CVE_Management_API
```
2. Create a Virtual Environment:

- On Windows:
```bash
  python -m venv venv
  venv\Scripts\activate
```
- On macOS and Linux:
```bash
  python3 -m venv venv
  source venv/bin/activate
```
3. Install Dependencies:
```bash
  pip install -r requirements.txt
```


## Setup and Running the Application

1. Prepare the Database:
- Ensure the `cve_database.csv` file is in the root directory.
- Run the data import script to populate the database:
```bash
  python data_import.py
```

2. Run the Flask Application:
```bash
  python run.py
```
The application will start and be accessible at `http://127.0.0.1:5000`.


## API Endpoints

### Get All CVEs

```http
  GET /cve/all
```

| Method    | URL        | Description                |
| :-------- | :--------- | :------------------------- |
| `GET`     | `/cve/all` | `Retrieve all CVEs`        |

### Get a Specific CVE by ID

```http
  GET /cve/<cve_id>
```

| Method    | URL             | Description                | Example                                      |
| :-------- | :-------------- | :------------------------- | :------------------------------------------- |
| `GET`     | `/cve/<cve_id>` | `Retrieve a CVE by its ID` | ``http://127.0.0.1:5000/cve/CVE-2021-32628`` |

### Add a New CVE

```http
  POST /cve/addCVE
```

| Method    | URL           | Description     |
| :-------- | :-----------  | :-------------- |
| `POST`    | `/cve/addCVE` | `Add a new CVE` |

Body
```json
{
  "cve_id": "CVE-1234-5678",
  "severity": "High",
  "cvss": 9.8,
  "affected_packages": "package1, package2",
  "description": "Sample CVE description",
  "cwe_id": "CWE-123"
}
```

### Update an Existing CVE

```http
  PUT /cve/<cve_id>
```

| Method    | URL             | Description              |
| :-------- | :-------------- | :----------------------- |
| `PUT`     | `/cve/<cve_id>` | `Update a CVE by its ID` |

Body
```json
{
  "severity": "Medium",
  "cvss": 5.5,
  "affected_packages": "package3, package4",
  "description": "Updated CVE description",
  "cwe_id": "CWE-456"
}
```

### Delete a CVE

```http
  DELETE /cve/<cve_id>
```

| Method    | URL             | Description              | Example                                    |
| :-------- | :-------------- | :----------------------- | :----------------------------------------- |
| `DELETE`  | `/cve/<cve_id>` | `Delete a CVE by its ID` | `http://127.0.0.1:5000/cve/CVE-2021-32628` |


## Testing with Postman

1. Open Postman.
2. Create a New Request:
- For each endpoint, set up a new request in Postman with the appropriate method, URL, headers, and body.
3. Send Requests:
- Send the requests to test the functionality of the API.
4. Verify Responses:
- Check the responses to ensure the API is functioning correctly.
