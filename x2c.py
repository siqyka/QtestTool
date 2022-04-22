from flask import Blueprint
from flask import  render_template, url_for, request
from flask import make_response, send_from_directory
from werkzeug.utils import secure_filename
import os
from apps.xmind2caseapp import write2excel, xmind2case

x2c = Blueprint('x2c',__name__) 
# workpath = os.getcwd()
workpath=os.path.dirname(os.path.realpath(__file__))
upload_dir = os.path.join(workpath, "apps/xmind2caseapp" ,"upload")
download_dir = os.path.join(workpath,"apps/xmind2caseapp" , "download")

@x2c.route("/index")
def x2ch():
    return render_template("x2c/x2c.html")

@x2c.route("/x2conf")
def x2conf():
    return render_template("x2c/x2c.html")


@x2c.route('/uploader', methods=['GET', 'POST'])
def uploader():
    # print(os.path.join(workpath))

    if request.method == 'POST':
        f = request.files['file']
        if f.filename[f.filename.find("."):]!=".xmind":
            return "X101"  # X101:上传的不是xmind格式
        filename = f.filename[:f.filename.find(".")]+".xls"
        uppath = os.path.join(upload_dir, secure_filename(f.filename))
        dopath = os.path.join(download_dir, filename)
        f.save(uppath)
        p = xmind2case.xmind2dict(uppath)
        h = xmind2case.handle_xmind_msg(p)
        write2excel.writr_to_excel(dopath, h)

        dpath = url_for("x2c.download_file", filename=filename)
        print(dpath)
        return "True+"+dpath

    else:
        return 'False+'
        # return render_template('upload.html')


@x2c.route("/download/<filename>", methods=['GET'])
def download_file(filename):
    # directory=os.path.join(workpath,"download")
    response = make_response(send_from_directory(
        download_dir, filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={}".format(
        filename.encode().decode('latin-1'))
    return response



