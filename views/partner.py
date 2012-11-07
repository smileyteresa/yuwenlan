# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, request, session, url_for
from models.users import users
from utils.users import require_login
from database import db

ywl = Blueprint('partner', __name__, template_folder = 'templates')

@ywl.route('/<username>/')
@require_login
def index(username):
    return render_template('partner/index.html', menu = 'home')

@ywl.route('/modify/<username>')
def modify(username):
    return username

@ywl.route('/talk/')
@require_login
def talk():
    if None in request.form.items():
        return '请填写内容'

    info = request.form