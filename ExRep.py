import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/about.html", methods=['POST','GET'])
def about():
    return render_template("about.html")

@app.route("/faq.html",  methods=['POST','GET'])
def faq():
    return render_template("faq.html")

@app.route("/content.html", methods=['POST','GET'])
def content():
    return render_template("content.html")

def val_predict(list_predict):
    to_predict = np.array(list_predict)
    # data = [[float(bmi)]]
    # .reshape(1, 12)
    loaded_model =  pickle.load(open('model.pkl', "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


    # int_features = [int(x) for x in request.form.values()]
    # final_feature = [np.array(int_features)]
    # prediction = model.predict(final_feature)

    # output = round(prediction[0], 2)

    # return render_template("content.html", prediction_text = 'Expenditure is $ {}'.format(output))
@app.route("/results", methods=["POST"])
def results():

    if request.method == "POST":
        list_predict = request.form.to_dict()
        list_predict = list(list_predict.values)
        result = val_predict(list_predict)
        prediction = result
    return render_template("result.html")

    # data = request.get_json(force=True)
    # prediction = model.predict([np.array(list(data.values()))])

    # output=prediction[0]
    # return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
