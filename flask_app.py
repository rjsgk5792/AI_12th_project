from flask import Flask, render_template, request
import pickle
import numpy as np

# model = pickle.load(open('cafe.pkl','rb'))

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('home.html')
    
    @app.route('/predict', methods=['POST'])
    def home():
        data1 = request.form['a'] # a,b,c,d 는 사용자 입력값
        data2 = request.form['b']
        data3 = request.form['c']
        data4 = request.form['d']
        arr = np.array([[data1, data2, data3, data4]])
        # pred = model.predict(arr)
        return render_template('after.html') #data=pred)
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)