#!flask/bin/python
import os
from app import app

port = os.environ.get("PORT") or 5000
app.run("0.0.0.0", port)
