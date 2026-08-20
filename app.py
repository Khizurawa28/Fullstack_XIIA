from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')

def home():
    return jsonify({
        "status": "success",
        "message": "Selamat datang di API Backend AI Capstone (V1)!"
    })

if __name__ == '__main__':
    # host='0,0,0,0' wajib digunakan agar server Flask di dalam container
    # bisa diakses dari luar container (komputer host)
    app.run(host='0.0.0.0', port=5000)