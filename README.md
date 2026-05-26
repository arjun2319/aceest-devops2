# ACEest Fitness & Gym - DevOps Assignment

## Project Overview
A Flask web API for ACEest Fitness & Gym management system.
Built as part of the Introduction to DevOps assignment (CSIZG514/SEZG514).
Demonstrates Version Control, Containerization, and CI/CD pipelines.

## Project Structure
aceest-devops/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── test_app.py                     # Pytest test suite
├── Dockerfile                      # Docker container config
├── .github/
│   └── workflows/
│       └── main.yml                # GitHub Actions CI/CD pipeline
└── README.md                       # Project documentation

## Local Setup and Execution

### Prerequisites
- Python 3.9+
- pip
- Docker (optional)

### 1. Clone the repository
git clone https://github.com/arjun2319/aceest-devops2.git
cd aceest-devops2

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the application
python app.py

### 4. Access the API endpoints
- GET  http://127.0.0.1:5000/           - Welcome message
- GET  http://127.0.0.1:5000/programs   - List all programs
- GET  http://127.0.0.1:5000/program/<name> - Get program details
- POST http://127.0.0.1:5000/calories   - Calculate calories

### 5. Example POST request
curl -X POST http://127.0.0.1:5000/calories \
  -H "Content-Type: application/json" \
  -d '{"weight": 70, "program": "Fat Loss (FL)"}'

## Running Tests Manually

### Run all tests
pytest test_app.py -v

### Expected output
test_app.py::test_home PASSED
test_app.py::test_get_programs PASSED
test_app.py::test_get_valid_program PASSED
test_app.py::test_get_invalid_program PASSED
test_app.py::test_calculate_calories PASSED
test_app.py::test_calories_missing_fields PASSED
6 passed

## Docker Setup

### Build the Docker image
docker build -t aceest-fitness .

### Run the container
docker run -p 5000:5000 aceest-fitness

### Access the app
http://localhost:5000

## GitHub Actions Integration

### How it works
Every push or pull request to the main branch automatically triggers the pipeline.

### Pipeline Stages
1. Checkout Code     - Pulls latest code from GitHub
2. Setup Python 3.9  - Installs Python environment
3. Install Dependencies - Runs pip install -r requirements.txt
4. Lint with flake8  - Checks code for syntax errors
5. Run Pytest        - Executes all 6 unit tests
6. Build Docker      - Builds the Docker image

### Pipeline file location
.github/workflows/main.yml

## Jenkins Integration

### How it works
Jenkins provides a secondary BUILD validation layer.
It pulls the latest code from GitHub and runs a clean build
to ensure code integrates correctly in a controlled environment.

### Jenkins BUILD Steps
1. Pull code from GitHub repository
2. Create Python virtual environment
3. Install dependencies via pip
4. Run Pytest test suite
5. Report build success or failure

### Jenkins Setup Instructions
1. Run Jenkins via Docker:
   docker run -d -p 8080:8080 jenkins/jenkins:lts

2. Create a Freestyle project named aceest-devops2

3. Under Source Code Management select Git and enter:
   https://github.com/arjun2319/aceest-devops2.git

4. Under Build Steps add Execute shell:
   python3 -m venv venv
   . venv/bin/activate
   pip install flask pytest
   pytest test_app.py -v

5. Click Build Now - build should complete with SUCCESS

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Welcome message |
| GET | /programs | List all fitness programs |
| GET | /program/<name> | Get program workout and diet |
| POST | /calories | Calculate daily calories |

## Programs Available
- Fat Loss (FL) - Calorie factor: 22
- Muscle Gain (MG) - Calorie factor: 35
- Beginner (BG) - Calorie factor: 26