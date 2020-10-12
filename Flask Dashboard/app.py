from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import json
import plotly
import plotly.graph_objs as go
import pickle

def create_plot():

    df = pd.read_csv('bank_new.csv') # creating a sample dataframe

    data = [

        go.Pie(
            labels = ['{}'.format(i) for i in list(df['y'].unique())],
            values = [36548, 4640],
            textinfo='label+percent',
            textposition='inside',
            hole = .3,
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


app = Flask(__name__)
importModel = pickle.load(open('RandomForest.sav', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict")
def pred():
    return render_template("predict.html")

@app.route("/visual")
def visual():
    bar = create_plot()
    return render_template('visual.html', plot=bar)


@app.route("/DataFrame")
def data():
    data = pd.read_csv('bank_new.csv')
    df = data.head(50).to_html(classes = 'data')
    return render_template('data.html',  tables=[df])

@app.route("/result", methods = ["POST","GET"])
def result():
    if request.method == "POST":
        input = request.form

        cpi = float(input['cpi'])

        cci = float(input['cci'])

        euribor = float(input['euribor'])

        employee = float(input['employee'])

        var = float(input['var'])
        
        age = int(input['age'])
        
        job = input['job']
        if job == 'admin.':
            strJob = 'Admin'
            dataJob = 'admin.'
        elif job == 'blue-collar':
            strJob = 'Blue-Collar'
            dataJob = 'blue-collar'
        elif job == 'entrepreneur':
            strJob = 'Entrepreneur'
            dataJob = 'entrepreneur'
        elif job == 'housemaid':
            strJob = 'Housemaid'
            dataJob = 'housemaid'
        elif job == 'management':
            strJob = 'Management'
            dataJob = 'housemaid'
        elif job == 'retired':
            strJob = 'Retired'
            dataJob = 'retired'
        elif job == 'self-employed':
            strJob = 'Self-employed'
            dataJob = 'self-employed'
        elif job == 'services':
            strJob = 'Services'
            dataJob = 'services'
        elif job == 'student':
            strJob = 'Student'
            dataJob = 'services'
        elif job == 'technician':
            strJob = 'Technician'
            dataJob = 'technician'
        else:
            strJob = 'Unemployed'
            dataJob = 'unemployed'

        marital = input['marital']
        if marital == 'married':
            strMarital = 'Married'
            dataMarital = 'married'
        elif marital == 'single':
            strMarital = 'Single'
            dataMarital = 'single'
        else:
            strMarital = 'Divorced'
            dataMarital = 'divorced'

        default = input['default']
        if default == 'yes':
            strDefault = 'Yes'
            dataDefault = 'yes'
        elif default == 'no':
            strDefault = 'No'
            dataDefault = 'yes'
        else:
            strDefault = 'Unknown'
            dataDefault = 'unknown'

        month = input['month']
        if month == 'jan':
            strMonth = 'January'
            dataMonth = 'january'
        elif month == 'feb':
            strMonth = 'February'
            dataMonth = 'february'
        elif month == 'mar':
            strMonth = 'March'
            dataMonth = 'march'
        elif month == 'apr':
            strMonth = 'April'
            dataMonth = 'april'
        elif month == 'may':
            strMonth = 'May'
            dataMonth = 'may'
        elif month == 'june':
            strMonth = 'June'
            dataMonth = 'june'
        elif month == 'july':
            strMonth = 'July'
            dataMonth = 'july'
        elif month == 'aug':
            strMonth = 'August'
            dataMonth = 'august'
        elif month == 'sep':
            strMonth = 'September'
            dataMonth = 'september'
        elif month == 'oct':
            strMonth = 'October'
            dataMonth = 'october'
        elif month == 'nov':
            strMonth = 'November'
            dataMonth = 'november'
        else:
            strMonth = 'December'
            dataMonth = 'december'

        campaign = int(input['campaign'])

        contact = input['contact']
        if contact == 'telephone':
            strContact = 'Telephone'
            dataContact = 'telephone'
        else:
            strContact = 'Cellular'
            dataContact = 'cellular'

        poutcome = input['poutcome']
        if poutcome == 'success':
            strPoutcome = 'Success'
            dataPoutcome = 'success'
        elif poutcome == 'failure':
            strPoutcome = 'Failure'
            dataPoutcome = 'failure'
        else:
            strPoutcome = 'Nonexistent'
            dataPoutcome = 'nonexistent'


        education = input['education']
        if education == 'basic.4y':
            strEducation = 'Basic.4y'
            dataEducation = 'basic.4y'
        elif education == 'basic.6y':
            strEducation = 'Basic.6y'
            dataEducation = 'basic.6y'
        elif education == 'basic.9y':
            strEducation = 'Basic.9y'
            dataEducation = 'basic.9y'
        elif education == 'high.school':
            strEducation = 'High School'
            dataEducation = 'high.school'
        elif education == 'professional.course':
            strEducation = 'Professional Course'
            dataEducation = 'professional.course'
        elif education == 'university.degree':
            strEducation = 'University Degree'
            dataEducation = 'university.degree'
        



        feature = pd.DataFrame({
            'age' : [age],
            'job' : [dataJob],
            'marital' : [dataMarital],
            'education' : [dataEducation],
            'default' : [dataDefault],
            'contact' : [dataContact],
            'month' : [dataMonth],
            'campaign' : [campaign],
            'poutcome' : [dataPoutcome],
            'emp.var.rate' : [var],
            'cons.price.idx' : [cpi],
            'cons.conf.idx' : [cci],
            'euribor3m' : [euribor],
            'nr.employed' : [employee]
        })

        proba = importModel.predict_proba(feature)[:,1]
        print(proba)

        if proba < 0.5:
            rslt = 'Client would not Subscribed'
        else:
            rslt = 'Client would Subscribed'

        return render_template('result.html', cpi = cpi, cci = cci, var = var, euribor = euribor, age = age, 
            job = strJob, marital = strMarital, month = strMonth, default = strDefault, contact = strContact, campaign = campaign,
            poutcome = strPoutcome, education = strEducation, employee = employee, result = rslt)




if __name__ == '__main__':
    app.run(debug=True, port = 8050)