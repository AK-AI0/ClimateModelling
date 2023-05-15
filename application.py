from flask import Flask, request, render_template,jsonify
from flask_cors import CORS,cross_origin
from src.pipeline.predict_pipeline import CustomData
from src.logger import logging

application = Flask(__name__)

app = application

@app.route('/')
@cross_origin()
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            col = request.form.get('col')

        )

        pred_df = data.get_data_as_dataframe()
        
        print(pred_df)

        return render_template('home.html',results = pred_df)
    
# @app.route('/predictAPI',methods=['POST'])
# @cross_origin()
# def predict_api():
#     if request.method=='POST':
#         data = CustomData(
#             col = request.json['col']
#         )

#         pred_df = data.get_data_as_dataframe()

#         dct = {'price':round(pred_df)}
#         return jsonify(dct)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)