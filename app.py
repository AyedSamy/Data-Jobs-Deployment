from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import pickle


app = Flask(__name__)
model = pickle.load(open('gbt_model.pkl','rb'))
scaler = pickle.load(open('test_scaler.pkl','rb'))

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('salary-prediction-form.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        state_dict = {'AZ':0,'CA':1,'CO':2,'DE':3,'FL':4,'GA':5,'IL':6,'IN':7,'KS':8,'NC':9,
                         'NJ':10,'NY':11,'OH':12,'PA':13,'SC':14,'TX':15,'UT':16,'UK':17,'VA':18,'WA':19}
        sector_dict = {'accounting':0,'aero':1,'agriculture':2,'arts':3,'biotech':4,'b_services':5, 'construction':6, 'c_services':7, 'educ':8, 'finance':9,'government':10, 'health_care':11,'it':12,'insurance':13,'manufacturing':14,'media':15,'mining':16, 'non_profit':17, 'oil_gas':18,'real_estate':19,'restaurants':20,'retail':21,'telecom':22,'transport':23,'travel':24}
        ownership_dict = {'college':0,'private':1,'public':2,'contract':3, 'franchise':4, 'government':5, 'hospital':6, 'non_profit':7,
                          'other':8, 'private_practice':9, 'school':10, 'self_employed':11,'subsidiary':12}
        position_dict = {'bi_analyst':0,'d_analyst':1,'d_architect':2,'d_engineer':3,'d_scientist':4,'ml_engineer':5,'other':6}
        
        rating = float(request.form['rating'])
        size = float(request.form['size'])
        revenue = float(request.form['revenue'])
        experience = float(request.form['exp_lvl'])
        
        states = np.zeros(len(state_dict))
        state = request.form['state']
        states[state_dict[state]] = 1   
        
        sectors = np.zeros(len(sector_dict))
        sector = request.form['sector']
        sectors[sector_dict[sector]] = 1
        
        ownerships = np.zeros(len(ownership_dict))
        ownership = request.form['ownership']
        ownerships[ownership_dict[ownership]] = 1
        
        positions = np.zeros(len(position_dict))
        position = request.form['position']
        positions[position_dict[position]] = 1
        
        inputs = np.concatenate((np.array([rating]),np.array([size]),np.array([revenue]),np.array([experience]),states,sectors,ownerships,positions)).reshape(1,-1)
        inputs = scaler.transform(inputs)
        
        return render_template('salary-predicted.html', prediction=round(model.predict(inputs)[0]*1000, 2))
    else:
        return render_template('salary-prediction-form.html')

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)