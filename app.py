from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS 

# Must Install 
# python -m pip install flask flask-cors

app = Flask(__name__)
CORS(app) 

@app.route('/run', methods=['POST'])
def run_python_code():
    data = request.json
    code = data.get('code', '')

    try:
        # Write code to a temporary file
        with open("temp_code.py", "w") as f:
            f.write(code)

        # Run the Python file and capture the output
        result = subprocess.run(["python", "temp_code.py"], capture_output=True, text=True, timeout=10)

        return jsonify({
            "stdout": result.stdout,
            "stderr": result.stderr
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
