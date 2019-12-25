from flask import Flask

app = Flask(__name__)

@app.route('/')
def check():
    return 'GrayModel (1,1) is up and Running'

if __name__ == '__main__':
    app.run(debug=True)