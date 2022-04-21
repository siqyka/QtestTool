# coding:utf-8 
from flask import Flask,render_template 
from x2c import x2c


app=Flask(__name__) 
app.register_blueprint(x2c,url_prefix='/x2c') 

@app.route("/index")
def index():
    # return send_file('templates/HangzhouMetroPlanning.html')
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500
  
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
else:
    application = app