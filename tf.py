from flask import Blueprint
from flask import  render_template,request
from flask import jsonify
from apps.testFakerapp import testFaker
import json

tf = Blueprint('tf',__name__) 


@tf.route("/index")
def testfakerh():
    return render_template("TF/testfaker.html")


@tf.route("/delete",methods=['POST'])
def tfdelete():
    if request.data:
        pram=json.loads(request.data.decode())
        retest=testFaker.delete_tf(pram["pkey"])
        return str(retest)
    else:
        return "False"

@tf.route("/modify",methods=['POST'])
def tfmodify():
    if request.data:
        pram=json.loads(request.data.decode())
        print(pram)
        retest=testFaker.modify_tf(pram["pkey"],pram["path"],pram["returnstr"])
        return str(retest)
    else:
        return "False"

@tf.route("/total")
def tftotal():
    return jsonify(testFaker.get_tfs())

@tf.route("/testfaker/<path:apath>", methods=['GET','POST'])
def tffaker(apath):
    retest=testFaker.tf_faker(apath)
    return retest