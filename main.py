# import "packages" from flask
from flask import Flask, render_template, request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/armaan/')
def walruses():
    return render_template("armaan.html")


@app.route('/chris/')
def hawkers():
    return render_template("chris.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/daniel/')
def daniel():
    return render_template("daniel.html")

@app.route('/about-us/')
def aboutus():
    return render_template("about-us.html")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")


# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
