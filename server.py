from flask import Flask,request, jsonify,render_template
import util
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/get_location_names')

def get_location_names():
    response = jsonify({
        'locations':util.get_loaction_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
@app.route('/predict_home_price',methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])
    response=jsonify({
        'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
if __name__=="__main__":
    util.load_saved_artifacts()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

