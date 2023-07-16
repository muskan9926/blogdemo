from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='e9f92153605cffb3e7ee85f6147c9fc1'

posts=[
    {
        'author':'muskan',
        'title':'blog post 1',
        'content':'first blog content',
         'date':'march 2003'
    },
    {
        'author':'khushi',
        'title':'blog post 2',
        'content':'second blog content',
         'date':'march 2018'
    }
]
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='about')

@app.route("/Register",methods=['GET','POST'])
def register():
   form=RegistrationForm()
   if form.validate_on_submit():
       flash(f'Acount create for {form.username.data}!','success')
       return redirect(url_for('home'))
   return render_template('register.html',title='register',form=form)

@app.route("/Login",methods=['GET','POST'])
def login():
   form=LoginForm()
   if form.validate_on_submit():
       if form.email.data== 'mus@gmail.com' and form.password.data == 'password':
         flash(f'You Have Logged In !','success')
         return redirect(url_for('home'))
       else:
        flash(f"Log In Unsuccesful!",'danger')
   return render_template('login.html',title='register',form=form)

if __name__ == '__main__':
    app.run(debug=True)