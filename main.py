from flask import Flask,render_template
import requests
URL="https://api.npoint.io/74c39ef081b37cda737e"
app = Flask(__name__)

@app.route('/')
def blog():
    response=requests.get(url=URL)
    all_posts=response.json()
    return render_template("index.html",posts=all_posts)

@app.route('/post/<int:id>')
def post_blog(id):
    response=requests.get(url=URL)
    all_posts=response.json()
    return render_template("post.html",posts=all_posts,id=id)

if __name__=="__main__":
    app.run(debug=True)

