from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:0812@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(500))

    def __init__(self, title,body):
        self.title = title
        self.body = body
        
@app.route('/',methods = ['POST', 'GET'])
def home_page():

    blogs = Blog.query.all()
    blog_id= request.args.get('id')
    
    if blog_id == None:
        return render_template('blog.html', 
        title="Build a Blog!", blogs=blogs )
        
    blog = Blog.query.get(blog_id)
        
    return render_template('single_blog.html'
        ,blog=blog)

@app.route('/newpost',methods = ['POST', 'GET'])
def add_blog():

    if request.method == 'POST':

        title = request.form['title']
        body = request.form['body']
        new_blog = Blog(title,body)
        
        db.session.add(new_blog)
        db.session.commit()
        
        new_page = Blog.query.order_by('-Blog.id').first()
        
        
        
        return redirect('/?id={}'.format(blog))

    else:
        return render_template('newpost.html',title="Add a Blog Post")

if __name__ == '__main__':
    app.run()