from flask import Flask, render_template, request
from subprocess import call
import numpy as np
import pickle
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/acknowledgement')
def acknowledgement():
    return render_template('acknowledgement.html')


@app.route('/home')
def main():
    return render_template('home.html')


@ app.route('/loginpage')
def loginpage():
    return render_template('loginpage.html')


@ app.route('/predict/', methods=['GET', 'POST'])
def predict():

    if request.method == "POST":
       # get form data
        temperature = request.form.get('temperature')
        fuel_price = request.form.get('fuel_price')
        cpi = request.form.get('cpi')
        unemployment = request.form.get('unemployment')
        size = request.form.get('size')
        holiday = request.form.get('holiday')
        type_b = request.form.get('type_b')
        type_c = request.form.get('type_c')

        # call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(
                temperature, fuel_price, cpi, unemployment, size, holiday, type_b, type_c)
            output = round(prediction[0])
            # pass prediction to template
            return render_template('predict.html', prediction=prediction)

        except ValueError:
            return "Please Enter valid values"

        pass
    pass


def preprocessDataAndPredict(temperature, fuel_price, cpi, unemployment, size, holiday, type_b, type_c):

    # keep all inputs in array
    test_data = [float(temperature), float(fuel_price), float(cpi), float(
        unemployment), int(size), int(holiday), int(type_b), int(type_c)]
    print(test_data)

    # convert value data into numpy array
    test_data = np.array(test_data)

    # reshape array
    test_data = test_data.reshape(1, -1)
    print(test_data)

    # open file
    file = open('salesfores.pkl', 'rb')

    # load trained model
    trained_model = pickle.load(file)

    # predict
    prediction = trained_model.predict(test_data)
    print(prediction)
    return prediction

    pass


if __name__ == '__main__':
    app.run(debug=True)
