from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Tap.Az API xos geldiniz",
        "official_site": "https://tap.az"
    })

if __name__ == "__main__":
    app.run(debug=True)