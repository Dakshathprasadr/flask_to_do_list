# Mistake 1

SQLAl   'l'   used in  SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'



# Mistake 2

<!-- mistake you used {{u.first_name}} but you should use {{u.f_name}} which used in f_name as database class-->

# Mistake 3

@ missed  in @app.route('/')


# Mistake 4

I did not mentioned () in  with app.app_context():

# Mistake 5

I did not mentioned thw whole line   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Mistake 6

I did mentioned [,] between like /insert" , method= "post" 

<form action="/insert" method= "post" >


# Mistake 7

I did not mentioned return statement in 

	return redirect('/')
    else:
        return redirect('/')