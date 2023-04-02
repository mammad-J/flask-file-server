from flask import Flask
from flask import render_template
import modules

app = Flask(__name__)
path = modules.home_directory()
dir_name = path.split("/")[-1]
dir_list = modules.dir_list(path)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", dir_name=dir_name, dir_list=dir_list)


if __name__ == "__main__":
    app.run(debug=True)