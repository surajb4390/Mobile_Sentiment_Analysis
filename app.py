from flask import Flask,render_template,request
import pickle
import sklearn

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))
cvt = pickle.load(open('vectorizer.pkl','rb'))


@app.route('/')
def Input():
    return render_template('index.html')




@app.route('/submit',methods=['GET','POST'])
def submit():
    message = request.form['message']
    input = cvt.transform([message])
    output = model.predict(input)
    return render_template('output.html',data=output)




if __name__=="__main__":
    app.run(debug=True)
