import random
from flask import Flask
app = Flask(__name__)

#Decided to pre-generate essays due to high server costs to run GPT-2
f = open("generated.txt", "r").read()

essays = f.split("SPLIT_CHARACTERS")

@app.route('/')
def index():
    return random.choice(essays).replace("\n", "<br/>")