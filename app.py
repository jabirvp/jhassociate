from flask import Flask
from flask import render_template
from flask_mail import Message, Mail

app = Flask(__name__)
mail = Mail()

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'jhassociatemanjeri@gmail.com'
app.config['MAIL_PASSWORD'] = 'passme123!@#'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail.init_app(app)

@app.route("/")
def hello():
    return render_template('hello.html')
    
@app.route("/send")
def mail_send():
    msg = Message("Chameleon: Xpath check status",
                  sender="jhassociatemanjeri@gmail.com",
                  recipients=['jhassociatemanjeri@gmail.com'])
    msg.body = "testing all testing"
    mail.send(msg)
    return render_template('test.html')