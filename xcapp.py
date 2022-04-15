from fileinput import filename
from operator import imod
from flask import Flask, render_template, send_file, url_for, request
from flask import make_response, send_from_directory
from werkzeug.utils import secure_filename
import os
from apps.xmind2caseapp import write2excel, xmind2case

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd()
upload_dir = os.path.join(app.config['UPLOAD_FOLDER'], "upload")
download_dir = os.path.join(app.config['UPLOAD_FOLDER'], "download")


@app.route("/moco")
def moco():
    return "Hello moco!"


@app.route("/test")
def test():
    return render_template("test.html")


@app.route("/x2c")
def x2c():
    return render_template("x2c.html")


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    # print(os.path.join(app.config['UPLOAD_FOLDER']))

    if request.method == 'POST':
        f = request.files['file']
        if f.filename[f.filename.find("."):]!=".xmind":
            return "Q101"
        filename = f.filename[:f.filename.find(".")]+".xls"
        uppath = os.path.join(upload_dir, secure_filename(f.filename))
        dopath = os.path.join(download_dir, filename)
        f.save(uppath)
        p = xmind2case.xmind2dict(uppath)
        h = xmind2case.handle_xmind_msg(p)
        write2excel.writr_to_excel(dopath, h)

        dpath = url_for("download_file", filename=filename)

        return "True+"+dpath

    else:
        return 'False+'
        # return render_template('upload.html')


@app.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    # directory=os.path.join(app.config['UPLOAD_FOLDER'],"download")
    response = make_response(send_from_directory(
        download_dir, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(
        filename.encode().decode('latin-1'))
    return response


@app.route("/index")
def index():
    # return send_file('templates/HangzhouMetroPlanning.html')
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
else:
    application = app
