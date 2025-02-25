from flask import Flask, render_template, request

from process import get_prediction

app = Flask(__name__)

@app.route('/', methods=["get", "post"])
def hello():
    message = ""
    if request.method == "POST":
        area1 = request.form.get("area1")
        area2 = request.form.get("area2")
        area3 = request.form.get("area3")
        area4 = request.form.get("area4")
        area5 = request.form.get("area5")
        area6 = request.form.get("area6")
        area7 = request.form.get("area7")
        area8 = request.form.get("area8")
        area9 = request.form.get("area9")
        area10 = request.form.get("area10")
        area11 = request.form.get("area11")
        area12 = request.form.get("area12")
        try:
            area1 = float(area1)
            area2 = float(area2)
            area3 = float(area3)
            area4 = float(area4)
            area5 = float(area5)
            area6 = float(area6)
            area7 = float(area7)
            area8 = float(area8)
            area9 = float(area9)
            area10 = int(area10)
            area11 = float(area11)
            area12 = float(area12)
        except Exception as e:
            print(e)
            message += "Некорректный ввод."

        cost = get_prediction(area1,area2,area3,area4,area5,area6,area7,area8,area9,area10,area11,area12)
        message += f"Прочность при растяжении, МПа равна {cost} ."
    return render_template("index.html", message=message)

if __name__ == '__main__':
    app.run()