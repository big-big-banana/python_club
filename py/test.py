from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/run-python', methods=['POST'])
def run_python():
    code = request.json.get('code', '')
    try:
        # 使用 subprocess 执行 Python 代码
        result = subprocess.run(
            ['python', '-c', code],
            capture_output=True,
            text=True,
            timeout=10
        )
        output = result.stdout
        error = result.stderr
    except Exception as e:
        output = ''
        error = str(e)

    return jsonify({'output': output, 'error': error})


if __name__ == '__main__':
    app.run(debug=True)
