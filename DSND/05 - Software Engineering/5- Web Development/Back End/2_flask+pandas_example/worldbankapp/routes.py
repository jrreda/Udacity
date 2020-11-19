from worldbankapp import application
from flask import render_template
import pandas as pd
from wrangling_scripts.wrangling import data_wrangling

data = data_wrangling()

print(data)



@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')

@application.route('/project-one')
def project_one():
    return render_template('project_one.html')
