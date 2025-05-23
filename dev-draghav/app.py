from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from the DEV environment!This is a test for the dev!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
