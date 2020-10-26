import csv

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route("/")
def index():
    with open('./arquivo_lanches.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=';')
        first_line = True
        lanches = []
        for row in data:
            if not first_line:
                lanches.append({
                    "identificador": row[0],
                    "nome_usuario": row[1],
                    "altura": row[2],
                    "lactose": row[3],

                    "peso": row[4],
                    "atleta": row[5],
                })
            else:
                first_line = False

    return render_template("index.html", lanches=lanches)


if __name__ == "__main__":
    app.run()
