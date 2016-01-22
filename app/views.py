import os
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('layout.html')

if __name__ == "__main__":
    port = os.environ.get("PORT") or 5000
    app.run("0.0.0.0", port)
