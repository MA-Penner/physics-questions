from flask import Flask, render_template, request, jsonify
from sympy import symbols, simplify, sqrt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare_equation():
    data = request.get_json()
    user_equation = data['equation']
    result = check_equivalence(user_equation)
    return jsonify({"message": result})

def check_equivalence(user_eq):
    x, y, z = symbols('x y z')
    target_eq = (4*x + y**3 + sqrt(z))*(23*x**2 + 67*y - 12*z)
    user_eq_simplified = simplify(user_eq)
    target_eq_simplified = simplify(target_eq)

    # Check if the difference simplifies to zero
    if simplify(user_eq_simplified - target_eq_simplified) == 0:
        return "The equations are equivalent."
    else:
        return ("The equations are not equivalent. Your answer was: " + 
                str(user_eq_simplified) + 
                ". The right answer is: " + 
                str(target_eq_simplified))

    
if __name__ == '__main__':
    app.run(debug=True)


