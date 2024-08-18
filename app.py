from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///todo.db"
db=SQLAlchemy(app)


class Todo(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200), nullable=False)
    desc=db.Column(db.String(500), nullable=False)
    # date=db.Column(db.Date, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno}- {self.title}-{self.desc}"
    


with app.app_context():

    db.create_all()

@app.route("/", methods=['GET', 'POST'])
def home():
   

    if request.method=='POST':
        add_title=request.form['title']
        add_desc=request.form['desc']


        # print(request.form['title'])
        # print('post')
        todo=Todo(title=add_title, desc=add_desc)
    
    # print(todo_all)
    
        db.session.add(todo)
        

        db.session.commit()

    todos=Todo.query.all()
    return render_template('index.html',todos=todos)


@app.route("/delete/<int:n>", methods=['GET','POST'])
def delete(n):
    todo=Todo.query.filter_by(sno=n).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


@app.route("/edit/<int:n>", methods=['GET','POST'])
def edit(n):
    
    return render_template('edit.html',n=n)
@app.route("/edited/<int:n>",methods=['GET','POST'] )
def edited(n):
    todo=Todo.query.filter_by(sno=n).first()
    db.session.delete(todo)

    edit_title=request.form['edit_title']
    edit_desc=request.form['edit_desc']
    
    new=Todo(title=edit_title, desc=edit_desc)
    db.session.add(new)
    db.session.commit()

    return redirect("/")






    
    



if __name__=="__main__":

    app.run(debug=True)