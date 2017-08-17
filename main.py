from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True



@app.route("/", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify']
    email = request.form['email']
    usernameError = ""
    passwordError = ""
    vPasswordError = ""
    emailError = ""
    if username == "" or " " in username or len(username) < 3 or len(username) > 20: 
        usernameError = "Please enter a valid username"
    if password == "" or " " in password or len(password) < 3 or len(password) > 20:
        passwordError = "Please enter your password" 
    if verify_password == "" or " " in verify_password or len(verify_password) < 3 or len(verify_password) > 20:
        vPasswordError = "Please enter your password"   
    if email != "":
        if  " " in email or "@" not in email or "." not in email or len(email) < 3 or len(email) > 20:
            emailError = "Please reenter email"

    if password != verify_password:
        vPasswordError = "Passwords do not match"
    if usernameError == "" and passwordError == "" and vPasswordError == "" and emailError == "":
        return redirect("/welcome?username=" + username)
    return render_template("student_form.html", usernameError=usernameError, 
                            passwordError=passwordError, vPasswordError=vPasswordError, 
                            emailError=emailError, username=username, email=email)   

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return render_template('success.html', username=username)


@app.route("/")
def index():
    return render_template('student_form.html')


app.run()

