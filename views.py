from flask import render_template, redirect, url_for, flash
from forms import SignupForm, LoginForm
from models import User
from flask_login import login_user, current_user, login_required, logout_user
from app import app, db


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user, False)

        flash("Account created!")
        return redirect(url_for("index"))

    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is not None and user.check_password(form.password.data):

            login_user(user, form.remember_me.data)
            return redirect(url_for("index"))

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('index'))


@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

