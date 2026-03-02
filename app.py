from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from CI/CD!\n GET READY FOR THE BEST EXPERIENCE EVER!!! TEST AUTO DEPLOYMENT"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
