# ACEest Fitness & Gym - DevOps Assignment

## Project Overview
A Flask web API for ACEest Fitness & Gym built as part of the DevOps assignment.
Implements CI/CD pipelines using GitHub Actions and Jenkins.

## Project Structure
aceest-devops/
├── app.py
├── requirements.txt
├── test_app.py
├── Dockerfile
├── .github/workflows/main.yml
└── README.md

## Local Setup

### 1. Clone the repository
git clone https://github.com/arjun2319/aceest-devops2.git
cd aceest-devops2

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the application
python app.py

### 4. Access the API
- Home: http://127.0.0.1:5000
- Programs: http://127.0.0.1:5000/programs
- Program Detail: http://127.0.0.1:5000/program/Fat Loss (FL)
- Calories: http://127.0.0.1:5000/calories (POST)

## Running Tests Manually
pytest test_app.py -v

## Docker Setup
Build the image:
docker build -t aceest-fitness .

Run the container:
docker run -p 5000:5000 aceest-fitness

## GitHub Actions Pipeline
Triggered on every push and pull request to main branch.
Pipeline stages:
1. Checkout code
2. Set up Python 3.9
3. Install dependencies
4. Lint with flake8
5. Run pytest tests
6. Build Docker image

## Jenkins Setup
1. Install Jenkins locally
2. Create a new Freestyle project
3. Connect to GitHub repository
4. Add build step - Execute shell with these commands:
   pip install -r requirements.txt
   pytest test_app.py -v
5. Save and click Build Now