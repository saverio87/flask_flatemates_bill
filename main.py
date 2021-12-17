from flask.views import MethodView
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill.flat import Bill, Flatmate


app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')

class ResultsPage(MethodView):
    
    
    def post(self):

        self.days_total = 0
        bill_form = BillForm(request.form)
        
        bill = Bill(float(bill_form.amount.data), str(bill_form.period.data))
        
        flatmate1 = Flatmate(bill_form.name1.data, float(bill_form.days_in_house1.data))
        flatmate2 = Flatmate(bill_form.name2.data, float(bill_form.days_in_house2.data))
        flatmate3 = Flatmate(bill_form.name3.data, float(bill_form.days_in_house3.data))

        self.days_total = self.days_total + flatmate1.days_in_house + flatmate2.days_in_house + flatmate3.days_in_house

        self.inputs = {
            "flatmate1": flatmate1,
            "flatmate2": flatmate2,
            "flatmate3": flatmate3,
            "bill": bill,
            "days_total": self.days_total
        }

        return render_template('results.html', inputs=self.inputs) 
        # f"First flatmate pays {flatmate1.pays(bill,self.days_total)}"

class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)

class BillForm(Form):

    amount = StringField("Bill Amount: ")
    period = StringField("Bill period: ")
    num_flatmates = StringField("Num flatmates: ")

    name1 = StringField("First flatmate's name: ")
    days_in_house1 = StringField("First flatmate's days in house: ")

    name2 = StringField("Second flatmate's name: ")
    days_in_house2 = StringField("Second flatmate's days in house: ")

    name3 = StringField("Third flatmate's name: ")
    days_in_house3 = StringField("Third flatmate's days in house: ")

    button = SubmitField("Split the bill!")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule('/bill',  view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results',  view_func=ResultsPage.as_view('results_page'))


app.run(debug=True)