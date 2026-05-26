import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'running'

def test_get_programs(client):
    response = client.get('/programs')
    assert response.status_code == 200
    data = response.get_json()
    assert 'programs' in data
    assert len(data['programs']) == 3

def test_get_valid_program(client):
    response = client.get('/program/Fat Loss (FL)')
    assert response.status_code == 200
    data = response.get_json()
    assert 'workout' in data
    assert 'diet' in data
    assert 'calorie_factor' in data

def test_get_invalid_program(client):
    response = client.get('/program/InvalidProgram')
    assert response.status_code == 404

def test_calculate_calories(client):
    response = client.post('/calories', json={
        'weight': 70,
        'program': 'Fat Loss (FL)'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data['calories'] == 1540

def test_calories_missing_fields(client):
    response = client.post('/calories', json={'weight': 70})
    assert response.status_code == 400