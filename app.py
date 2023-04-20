from flask import Flask,render_template,request
from flask_mail import *
import random
from flask_mysqldb import MySQL
import mysql.connector
import os
import pandas as pd
import numpy as np
import pickle
app=Flask(__name__,template_folder='Template')


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='dabadeomkar737@gmail.com'
app.config['MAIL_PASSWORD']='bzocwddaeoomevpi'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)
otp=random.randint(0000,9999)

try:
    conn=mysql.connector.connect(host="localhost",user="root",password="omkar@123",database="loan")
    cursor=conn.cursor()
    #db=yaml.load(open('db.yaml'))
    app.config['MYSQL_HOST']='localhost'
    app.config['MYSQL_USER']='root'
    app.config['MYSQL_PASSWORD']='omkar@123'
    app.config['MYSQL_DB']='loan'
    mysql=MySQL(app)
except:
  print("An exception occurred")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index',methods=['GET','POST'])
def omkar():
    return render_template('signin.html')

@app.route('/omkarmod',methods=['POST'])
def omkarmod():
    email=request.form.get('uname')
    password=request.form.get('passf')
    cursor.execute("""SELECT * FROM signin WHERE email LIKE  '{}' AND password LIKE '{}' """.format(email,password))
    users=cursor.fetchall()
    print(users)
    if(len(users)>0):
      
        msg=Message("OTP",sender='dabadeomkar737@gmail.com',recipients=[email])
        msg.body=str(otp)
        mail.send(msg)
        return render_template('validate.html')
    else:
        b="Incorrect Username and Password"
        return render_template("signin.html",sin_text="{}".format(b))
    
    

@app.route('/about',methods=['GET','POST'])
def om():
      if request.method=='POST':
        userDetails=request.form
        name=userDetails['name']
        email=userDetails['email']
        password=userDetails['password']
        conform_p=userDetails['re_password']
        cur=mysql.connection.cursor()
        
        
        params = [email]
        
        
    # cursor return affected rows
        count = cur.execute('select * from signin where email=%s', params)  # prevent SqlInject
        params=[password]
        comp = cur.execute('select * from signin where password=%s', params)
        if count == 0 and comp==0:
            cur.execute("INSERT INTO signin(name,email,password,conform_p) VALUES(%s,%s,%s,%s)",(name,email,password,conform_p))
            mysql.connection.commit()
            cur.close()
            #a="<script> alert('<h1 >success</h1>')</script>"
            return render_template('signin.html')
       
        else:
             a="please Email id and password shoud be unique"
             return render_template("signupp.html",sign_text="{}".format(a))
     
      else:
        return render_template('signupp.html')



@app.route('/bada')
def form():
    return render_template("validate.html")

@app.route('/omkar')
def omkar1():
    return render_template('omkar.html')


@app.route('/validate',methods=['POST'])
def validate():
    userotp=request.form['otp']
    if otp==int(userotp):
        return render_template('omkar.html')
    else:
        h="Incorrect Otp"
        return render_template("validate.html",otp_txt="{}".format(h))


#bike price prediction

filename="model9.pkl"
fileobj=open(filename,'rb')
b1= pickle.load(fileobj)
@app.route('/bike')
def kaise():
    return render_template('motor1.html')

@app.route('/end')
def sanket():
    return render_template('motor.html')

@app.route('/predict1',methods=['POST'])
def predict1():
    if request.method=='POST':
        kms_driven=float(request.form['kms_driven'])
        year=float(request.form['age'])
        age=2023-year
        power=float(request.form['power'])
        owner=request.form['owner']
        if (owner=='Second_Owner'):
            Second_Owner=1
            First_Owner=0
        else:
            Second_Owner=0
            First_Owner=1
        

        prediction=b1.predict([[kms_driven,age,power,Second_Owner]])
        
        return render_template("motor.html",prediction_text="Total Motor Bike Price is Rs {} ".format(int(prediction)))

    else:
        return render_template('motor.html')



#bike rental prediction

filename="model6.pkl"
fileobj=open(filename,'rb')
b2= pickle.load(fileobj)
@app.route('/rental')
def main():
    return render_template('pico.html')

@app.route('/rentkiya')
def alankar():
    return render_template('form_bike.html')

@app.route('/predict2',methods=['POST'])
def predict2():
    if request.method=='POST':
       global holiday
    global weekday
    global workingday
    global weathersit

    if request.method=='POST':
        
        day=int(request.form['day'])
        mnth=int(request.form['mnth'])
        year=int(request.form['year'])
        season=str(request.form['season'])
        if season=="S P R I N G":
            int((season.replace("S P R I N G", "1")))
        elif season=="S U M M E R":
            int((season.replace("S U M M E R", "2")))
        elif season=="R A I N F A L L":
            int((season.replace("R A I N F A L L", "3")))
        elif season=="W I N T E R":
            int((season.replace("W I N T E R", "4")))

        
        holiday=str(request.form['holiday'])
        if holiday=="H O L I D A Y":
            int((holiday.replace("H O L I D A Y", "0")))
            
        elif holiday=="N O T H O L I D A Y":
            int((holiday.replace("N O T H O L I D A Y", "1")))
            

        weekday=str(request.form['weekday'])
        if weekday=="S U N D A Y":
            int((weekday.replace("S U N D A Y", "0")))
        
        elif weekday=="M O N D A Y":
            int((weekday.replace("M O N D A Y", "1")))
            
        elif weekday=="T U E S D A Y":
            int((weekday.replace("T U E S D A Y", "2")))
            
        elif weekday=="W E D N E S D A Y":
            int((weekday.replace("W E D N E S D A Y", "3")))
            
        elif weekday=="T H U R S D A Y":
            int((weekday.replace("T H U R S D A Y", "4")))
            
        elif weekday=="F R I D A Y":
            int((weekday.replace("F R I D A Y", "5")))
            
        elif weekday=="S A T U R D A Y":
            int((weekday.replace("S A T U R D A Y", "6")))
            

        workingday=str(request.form['workingday'])
        if workingday=="H O L I D A Y":
            int((workingday.replace("H O L I D A Y", "0")))
            
        elif workingday=="N O T H O L I D A Y":
            int((workingday.replace("N O T H O L I D A Y", "1")))
            

        weathersit=str(request.form['weathersit'])
        if weathersit=="Clear, Few clouds, Partly cloudy, Partly cloudy":
            int((weathersit.replace("Clear, Few clouds, Partly cloudy, Partly cloudy", "1")))
            
        elif weathersit=="Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist":
            int((weathersit.replace("Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist", "2")))
            
        elif weathersit=="Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds":
            int((weathersit.replace("Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", "3")))
        
        elif weathersit=="Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog":
            int((weathersit.replace("Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog", "4")))
        

        prediction=b2.predict([[day,mnth,year,season,holiday,weekday,workingday,weathersit]])
        
        return render_template("form_bike.html",prediction_text="Total Rent on that day is {} ".format(int(prediction)))

    else:
        return render_template('form_bike.html')


# car price prediction

filename="model13.pkl"
fileobj=open(filename,'rb')
b3= pickle.load(fileobj)
@app.route('/car')
def kaisecar():
    return render_template('car.html')

@app.route('/carform')
def murli():
    return render_template('car_form.html')

@app.route('/predict3',methods=['POST'])
def predict3():
    if request.method=='POST':
        Present_Price=float(request.form['Present_Price'])
        Kms_Driven=float(request.form['Kms_Driven'])
        age=int(request.form['no_year'])
        no_year=2023-age
        fuel=request.form['fuel']
        if(fuel=='Petrol'):
            Petrol=1.0
            Diesel=0.0
        else:
            Petrol=0.0
            Diesel=1.0

        seller_type=request.form['seller_type']
        if(seller_type=='Individual'):
            Individual=1.0
            Dealer=0.0
        else:
            Individual=0.0
            Dealer=1.0

        transmission=request.form['transmission']
        if(transmission=='Manual'):
            Manual=1.0
            Automatic=0.0
        else:
            Manual=0.0
            Automatic=1.0

        

        prediction=b3.predict([[Present_Price,Kms_Driven,no_year,Petrol,Individual,Manual]])
        
        return render_template("car_form.html",prediction_text="Total Car Price is Rs {:.2f} ".format(float(prediction)))

    else:
        return render_template('car_form.html')


if __name__=='__main__':
    app.run(debug=True,port=5)