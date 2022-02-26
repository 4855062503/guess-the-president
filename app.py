from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Returns index template '''
    if request.method == 'POST':
        if request.files['image']:
            return "has files"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
