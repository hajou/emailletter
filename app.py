from flask import Flask, render_template, redirect, url_for, request,session,flash
import requests 

app = Flask(__name__)


def subscribe_user(email, user_group_email, api_key):
	resp = requests.post(f"https://api.mailgun.net/v3/lists/{user_group_email}/members",
		auth=("api", api_key),
		data ={"subscribed": True,
			"address": email}
			)
	return resp

@app.route('/', methods=["GET", "POST"])
def index():
	if request.method == "POST":
		email = request.form.get('email')
		
		subscribe_user(email = email, user_group_email = "newsletter@sandbox7b20a4bdaa084d91afc2cd8ffc729507.mailgun.org", api_key = "fd72de5cc191d4e339d65a25cd0cb205-aff8aa95-6c51999c")

	return render_template("index.html")





if __name__ == '__main__':
	app.run(debug=True)
