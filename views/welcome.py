# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, request, session, url_for
from models.users import users
from database import db
ywl = Blueprint('welcome', __name__, template_folder = 'templates')

@ywl.route('/')
def index():
    return render_template('index.html')

@ywl.route('/welcome/', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        info = request.form
        if None in info.items():
            return '请填写参数'
        email = users.query.filter_by(email=info['email']).first()
        if email:
            return '邮箱已注册'
        username = users.query.filter_by(username=info['username']).first()
        if username:
            return '用户名已占用'
        user = users()
        user.email = info['email']
        user.username = info['username']
        user.password = info['password']
        db.session.add(user)
        db.session.commit()
        login(user, remember = False)
        return render_template('debug.html', debug = session)
    return render_template('signup.html')

@ywl.route('/whatsup/', methods = ['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        info = request.form

        if None in info.items():
            return '请填写参数'
        user = users.query.filter_by(email=info['email'], password=info['password']).first()
        if not user:
            return '用户名密码错误'

        #判断记住我
        if 'remember' in info:
            remember = True
        else:
            remember = False

        #登陆session
        login(user, remember)
        return redirect(url_for('.index'))

    return render_template('signin.html')

@ywl.route('/bye/')
def sign_out():
    try:
        session.pop('id')
        session.pop('username')
        session.pop('_permanent')
    except Exception:
        pass
    return redirect(url_for('.index'))
    #return render_template('debug.html', debug = session)

def login(user, remember):
    if not user:
        return None
    if remember is True:
        session.permanent = True
    session['id'] = user.id
    session['username'] = user.username
