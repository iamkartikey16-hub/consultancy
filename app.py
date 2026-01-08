from flask import Flask, render_template, request, redirect, url_for,  jsonify
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("bdipl0212@gmail.com")       # sender
SENDER_PASSWORD = os.getenv("uxolktesedudrlvm")      # Gmail App Password
RECEIVER_EMAIL = os.getenv("iamkartikey16@gmail.com")  # 🔥 where enquiries go

import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


@app.route("/submit-enquiry", methods=["POST"])
def submit_enquiry():
    name = request.form.get("name")
    company = request.form.get("company")
    email = request.form.get("email")
    mobile = request.form.get("mobile")
    message = request.form.get("message")

    msg = EmailMessage()
    msg["Subject"] = "New Enquiry - Kiran Consultancy Website"
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg.set_content(f"""
Name: {name}
Company: {company}
Email: {email}
Mobile: {mobile}

Message:
{message}
""")

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()

        return jsonify({"success": True})

    except Exception as e:
        print("❌ EMAIL ERROR:", e)
        return jsonify({"success": False}), 500


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/clientele")
def clientele():
    return render_template("clientele.html")

@app.route("/achievements")
def achievements():
    return render_template("achievements.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True)
