from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

from flask import Flask, request, jsonify

@app.route("/submit-enquiry", methods=["POST"])
def submit_enquiry():
    name = request.form.get("name")
    email = request.form.get("email")
    subject = request.form.get("subject")
    message = request.form.get("message")

    print("Enquiry:", name, email, subject, message)

    # Later: send email or save DB
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)
