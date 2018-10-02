from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:0812@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title,body):
        self.title = title
        self.body = body
        
@app.route('/',methods = ['POST', 'GET'])
def blog():

    blogs = Blog.query.all()
    return render_template('blog.html',title="Build a Blog!", 
        blogs=blogs)

@app.route('/newpost')
def add_blog():

    if request.method == 'POST':

        title = request.form['title']
        body = request.form['body']
        new_body=Blog(body)
        new_title = Blog(title)
        db.session.add(new_title)
        db.session.add(new_body)
        db.session.commit()

    return render_template('newpost.html')


if __name__ == '__main__':
    app.run()