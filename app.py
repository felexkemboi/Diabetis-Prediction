#print(model.predict([[1.8]]))

"""
from model import model 
print(model) """

import numpy as np
from flask import Flask, request, jsonify,render_template
import pickle

#creating instance of the class
app=Flask(__name__)
model = pickle.load(open('model.pkl','rb'))


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,8)
    loaded_model = pickle.load(open("model.pkl","rb"))
    result = loaded_model.predict(to_predict)
    return result[0]




#to tell flask what url shoud trigger the function index()
"""
@app.route('/')
def index():
    return render_template('index.html',model=model)
    """


@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())

        print(to_predict_list)

        to_predict_list = list(map(float, to_predict_list))
        print("yeees")

        print(to_predict_list)

        result = ValuePredictor(to_predict_list)
        print(result)

        if int(result)==1:
            prediction='Has Diabetes'
        else:
            prediction='Not Diabetic'
        print(prediction)
        return render_template("index.html",prediction=prediction)
    else:
    	return render_template("index.html")




if __name__ == '__main__':
    app.run(port=5000, debug=True)
