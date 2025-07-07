from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

# Store last quotes to avoid immediate repeat
last_normal = None
last_fun = None

# Function to load quotes from file
def load_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Function to get a quote that's not the same as last time
def get_unique_quote(quotes, last_quote):
    if len(quotes) <= 1:
        return quotes[0]
    
    quote = random.choice(quotes)
    while quote == last_quote:
        quote = random.choice(quotes)
    return quote

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-normal-quote')
def get_normal_quote():
    global last_normal
    quotes = load_quotes('normal_quotes.json')
    quote = get_unique_quote(quotes, last_normal)
    last_normal = quote
    return jsonify({'quote': quote})

@app.route('/get-fun-quote')
def get_fun_quote():
    global last_fun
    quotes = load_quotes('fun_quotes.json')
    quote = get_unique_quote(quotes, last_fun)
    last_fun = quote
    return jsonify({'quote': quote})

if __name__ == '__main__':
    app.run(debug=True)
