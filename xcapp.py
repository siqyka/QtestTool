from flask import Flask,render_template,send_file,url_for,url_for,request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "E:\\GIT\\xmind2casewww\\upload\\"

@app.route("/moco")
def moco():
    return "Hello moco!"

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/x2c")
def x2c():
    return render_template("x2c.html")

@app.route('/uploader',methods=['GET','POST'])
def uploader():
    print(os.path.join(app.config['UPLOAD_FOLDER']))

    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

        return 'file uploaded successfully'

    # else:
    #     return 'file uploaded f'
    #     # return render_template('upload.html')

@app.route("/index")
def index():
    # return send_file('templates/HangzhouMetroPlanning.html')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
else:
    application = app
