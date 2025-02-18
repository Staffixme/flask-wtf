from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    params = {}
    params["prof"] = prof
    params["img1"] = url_for("static", filename="img/1.jpg")
    params["img2"] = url_for("static", filename="img/2.jpg")
    return render_template('prof.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
