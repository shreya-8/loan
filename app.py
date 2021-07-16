from flask import Flask, escape, request, render_template
import pickle

app = Flask(__name__, template_folder='templetes')
model = pickle.load(open('classifier.pkl', 'rb'))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Gender = request.form['Gender']
        Married = request.form['Married']
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        LoanAmount = float(request.form['LoanAmount'])
        Credit_History = float(request.form['Credit_History'])

        if Gender == "Male":
            Gender = 0
        else:
            Gender = 1
 
        if Married == "Unmarried":
            Married = 0
        else:
            Married = 1
 
        if Credit_History == "Unclear Debts":
            Credit_History = 0
        else:
            Credit_History = 1

          
 
        LoanAmount = LoanAmount / 1000
 
        prediction = model.predict([[Gender, Married, ApplicantIncome, CoapplicantIncome, LoanAmount, Credit_History]])
     
        if prediction == 0:
            pred = 'Rejected'
        else:
            pred = 'Accepted'
    


        return render_template("index.html", prediction_text="Your loan is {}".format(pred))


    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


