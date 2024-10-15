from flask import Flask, render_template, request
from algorithms import naive_pattern_matching, rabin_karp_pattern_matching

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match_pattern():
    text = request.form['text']
    pattern = request.form['pattern']
    algorithm = request.form['algorithm']

    naive_matches = []
    rabin_karp_matches = []

    if algorithm == 'naive' or algorithm == 'both':
        naive_matches = naive_pattern_matching(text, pattern)

    if algorithm == 'rabin-karp' or algorithm == 'both':
        rabin_karp_matches = rabin_karp_pattern_matching(text, pattern)

    return render_template('result.html', 
                           text=text, 
                           pattern=pattern, 
                           naive_matches=naive_matches, 
                           rabin_karp_matches=rabin_karp_matches, 
                           algorithm=algorithm)

if __name__ == "__main__":
    app.run(debug=True)
