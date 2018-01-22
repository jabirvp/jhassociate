from flask import Flask, make_response, jsonify
from flask import render_template, request
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
	return render_template('index.html')

@app.route("/contact", methods=['POST'])
def contact():
	try:
		data = request.get_json()
		name = data.get('name')
		mob_number = data.get('mob_number')
		area = data.get('area')
		buisness = data.get('business')
		code = data.get('code')

		assert name
		assert mob_number
		assert area
		assert buisness
		assert code
	except AssertionError:
		return make_response(
			jsonify(message="Invalid request, params missing"),
			400
		)

	msg = Message("New customer enquiry in " + code,
				  sender="jhassociatemanjeri@gmail.com",
				  recipients=['jhassociatemanjeri@gmail.com'])
	msg.body = "Mobile Number : " + mob_number + "\nName : " + name + "\nArea : " + area + "\nBuisness : " + buisness + "\nCode Number : " + code 
	mail.send(msg)

	return jsonify(
		status = True,
		message = "A J&H Executive will contact you soon."
	)