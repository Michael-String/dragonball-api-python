from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://dragonball-api.com/api/characters?page=1&limit=10" 

@app.route('/')
def home():

    page = request.args.get('page', 1, type=int)

    limit = 10

    try:

        response = requests.get(
    f"https://dragonball-api.com/api/characters?page={page}&limit={limit}",
    timeout=20
        )

        response.raise_for_status()
        data = response.json()

        characters = data.get('items', [])

        meta = data.get('meta', {
            'currentPage': 1,
            'totalPages': 1
        })

    except Exception as e:

        print("ERROR:", e)

        characters = []

        meta = {
            'currentPage': 1,
            'totalPages': 1
        }

    return render_template(
        'index.html',
        characters=characters,
        meta=meta
    )

if __name__ == '__main__':
    app.run(debug=True)