import ast
from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL
from recommender.recommender import recommender
app = Flask(__name__)

mysql = MySQL()

#MySQL configurations
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='Bucketlist'
app.config['MYSQL_DATABASE-HOST']='localhost'
mysql.init_app(app)

@app.route("/main")
def home():
   return render_template('index.html')

@app.route("/showrecommend")
def showrecommend():
   return render_template('recommend.html')

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp',methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    if _name and _email and _password:
        return json.dumps({'html':'<span> All fields good!!</span>'})
    else:
        return json.dumps({'html':'<span> Enter the required fields</span>'})

@app.route('/recommendation',methods=['POST','GET'])
def reco():
   if request.method == 'POST':
      movieID=request.form['movieID']
      recommended=recommender(int(movieID),3)
      string_send =""
      for i in range(len(recommended)):
          string_send+= "<img src='{4}'><br/> Movie ID: {0} <br/> Movie Name: {1} <br/> Movie Genre: {2} <br/> Movie plot: {3}<br/><br/>".format(recommended[i][0],recommended[i][1],recommended[i][2],recommended[i][3],recommended[i][4])
      return render_template("recommendation.html", string=string_send)

@app.route('/showmovies')
def movies():
   return render_template('movies.html')

if __name__ == "__main__":
   app.run()
