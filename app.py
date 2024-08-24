from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)




ENV='dev'

if ENV =='dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/lexus'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']=''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)


class Feedback(db.Model):
    __tablename__='feedback'
    id=db.Column(db.Integer(), primary_key=True)
    customer=db.Column(db.String(100), unique=True)
    dealer=db.Column(db.String(100))
    rating=db.Column(db.Integer())
    comments=db.Column(db.Text())

    def __init__(self,customer,dealer,rating,comments):
        self.customer=customer
        self.dealer=dealer
        self.rating=rating
        self.comments=comments

with app.app_context():
    # Perform database operations here
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
     if request.method=='POST':
         
    # Retrieve form data
        customer= request.form.get('customer')
        dealer = request.form.get('dealer')
        rating = request.form.get('rating')
        comments = request.form.get('comments')
        if (customer=='' or dealer==''):
            return render_template('index.html', message='please select customer and dealer')
        if db.session.query(Feedback).filter(Feedback.customer==customer).count()==0:
            data=Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments)
            return render_template('submit.html')
        return render_template('index.html',message='You have already submitted response')
            
        

        return render_template('submit.html')
    
    # Here you can process the data, save it to a database, etc.
    
    # For this example, let's just print the data to the console
    
    
    

if __name__ == '__main__':
    app.run()
