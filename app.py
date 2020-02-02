from flask import Flask, render_template, redirect, url_for

# Create an instance of Flask
app = Flask(__name__)

# Route to render news1.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/about")
def aboutr():
    return render_template("about.html")

@app.route("/contact")
def news1():
    return render_template("contact.html")

@app.route("/projects")
def news2r():
    return render_template("projects.html")

@app.route("/skills")
def news3r():
    return render_template("skills.html")

if __name__ == "__main__":
    app.run()
