from flask import Flask, render_template, request, redirect, url_for,  jsonify
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "bdipl0212@gmail.com"        # sender
SENDER_PASSWORD = "uxolktesedudrlvm"       # Gmail App Password
RECEIVER_EMAIL = "iamkartikey16@gmail.com"  # 🔥 where enquiries go
from flask import Flask, request, jsonify

@app.route("/submit-enquiry", methods=["POST"])
def submit_enquiry():
    name = request.form.get("name")
    company = request.form.get("company")
    email = request.form.get("email")
    mobile = request.form.get("mobile")
    message = request.form.get("message")

    email_body = f"""
New Contact Enquiry Received

Name: {name}
Company: {company}
Email: {email}
Mobile: {mobile}

Message:
{message}
"""

    try:
        msg = EmailMessage()
        msg["Subject"] = "New Enquiry - Kiran Consultancy Website"
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL
        msg.set_content(email_body)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)

        return jsonify({"success": True})

    except Exception as e:
        print("Email error:", e)
        return jsonify({"success": False})


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
