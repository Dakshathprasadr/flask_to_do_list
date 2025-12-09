from flask import Flask, render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer ,primary_key = True,  )
    f_name = db.Column(db.String(20), unique=False, nullable= False)
    
    def __repr__(self):
        return f"Name: {self.f_name}" # Doubt

@app.route("/")

def home():
    use = User.query.all()
    return render_template("home.html", users_h = use)

#============================================================================

@app.route('/insert')
def add_user():
    return render_template('user_input.html')

@app.route('/insert' , methods=["POST", "GET"])
def users():
    first_name = request.form.get("first_name") #GET process in there


    if first_name != ' ': # if its not empty
        p = User(f_name = first_name) # import to db  
        db.session.add(p)  #POST process in there
        db.session.commit()

        return redirect('/')
    else:
        return redirect('/')
    
#============================================================================

@app.route('/delete/<int:id>')

def erase(id):
    data = User.query.get(id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')


#============================================================================


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)