from flask import Flask, render_template, request
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    ''' Returns index template '''
    if request.method == 'POST':
        if request.files['image']:
            upload_file = request.files['image']
            return str(base64.b64encode(upload_file.read()))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)
