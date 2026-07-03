from flask import Blueprint, flash, redirect, request, url_for, session, render_template
# 🛠️ Paths & Forms Imports Fixed (Correct spellings)
from app.forms import Registration_form, Login_form

auth_bp = Blueprint('auth', __name__)

# Temporary dictionary users store karne ke liye
USER_DATA = {}

@auth_bp.route('/register', methods=['POST', 'GET'])
def register():
    form = Registration_form()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        
        # User ko dictionary mein save kiya
        USER_DATA[name] = password
        
        flash(f"{name}, You Successfully Registered!", "success")
        return redirect(url_for("auth.login"))
        
    return render_template("register.html", form=form)


@auth_bp.route('/login', methods=["POST", "GET"])
def login():
    form = Login_form()
    
    # WTForms validation check for login
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # 🛠️ Bug Fixed: USER_DATA['username'] ki jagah dynamic variable USER_DATA[username] kiya
        if username in USER_DATA and USER_DATA[username] == password:
            session['user'] = username
            flash("Logged In Successfully!", 'success')
            return redirect(url_for('task.view_task')) # Agar task page par bhejna ho
        else:
            flash("Invalid Credentials, Try Again", "error")
            
    return render_template('login.html', form=form)


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged Out Successfully!", "success")
    return redirect(url_for('auth.login'))