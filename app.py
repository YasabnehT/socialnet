from flask import Flask, render_template,request
from flask_cors import CORS
from models import *
from waitress import serve
app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['POST', 'GET', 'DELETE', 'PUT'])
def index():
    if request.method =='GET':
        pass
    if request.method =='POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name, post)
    posts = get_posts()
    return render_template('index.html', posts=posts)

if __name__=='__main__':
    app.run(debug=True)
    #serve(app, host = '127.0.0.1', port = 5000)
