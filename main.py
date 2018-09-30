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

    def __init__(self, name):
        self.name = name
        
@app.route('/', methods=['POST', 'GET'])
def blog():

    if request.method == 'POST':
        blog_name = request.form['blog']
        new_blog = Task(blog_name)
        db.session.add(new_blog)
        db.session.commit()

    blogs = Blog.query.all()
    return render_template('blog.html',title="Build a Blog!", 
        blog=blog)


@app.route('/add-blog',methods =['POST'] )
def add_blog():

    
    

    return render_template('newpost.html')


if __name__ == '__main__':
    app.run()