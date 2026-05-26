from flask import Flask, jsonify, request

app = Flask(__name__)

PROGRAMS = {
    "Fat Loss (FL)": {
        "workout": "Mon: Back Squat 5x5, Tue: Bike, Wed: Bench Press, Thu: Deadlift, Fri: Cardio",
        "diet": "Egg Whites + Oats, Grilled Chicken, Fish Curry. Target: 2000 kcal",
        "calorie_factor": 22
    },
    "Muscle Gain (MG)": {
        "workout": "Mon: Squat 5x5, Tue: Bench 5x5, Wed: Deadlift, Thu: Front Squat, Fri: Rows",
        "diet": "Eggs + Oats, Chicken Biryani, Mutton Curry. Target: 3200 kcal",
        "calorie_factor": 35
    },
    "Beginner (BG)": {
        "workout": "Air Squats, Ring Rows, Push-ups. Focus: Technique",
        "diet": "Balanced Tamil Meals: Idli, Dosa, Rice + Dal. Protein: 120g/day",
        "calorie_factor": 26
    }
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to ACEest Fitness API", "status": "running"})

@app.route('/programs', methods=['GET'])
def get_programs():
    return jsonify({"programs": list(PROGRAMS.keys())})

@app.route('/program/<name>', methods=['GET'])
def get_program(name):
    if name not in PROGRAMS:
        return jsonify({"error": "Program not found"}), 404
    return jsonify(PROGRAMS[name])

@app.route('/calories', methods=['POST'])
def calculate_calories():
    data = request.get_json()
    weight = data.get('weight')
    program = data.get('program')
    if not weight or not program:
        return jsonify({"error": "weight and program are required"}), 400
    if program not in PROGRAMS:
        return jsonify({"error": "Invalid program"}), 404
    factor = PROGRAMS[program]['calorie_factor']
    calories = int(weight * factor)
    return jsonify({"weight": weight, "program": program, "calories": calories})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)