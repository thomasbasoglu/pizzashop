from cgitb import text
import csv
from flask import *
from datetime import *
from time import *
import sqlite3
import csv

app = Flask(__name__, template_folder='templates')
pizza = []


 

def dbSetup():
    con = sqlite3.connect('example.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE [IF NOT EXISTS] pizzashop( 
        primary_key_column int PRIMARY KEY,
        date_time date,
        order_number int, 
        price float
        )''')

def getTime():
   now = datetime.now()
   formatted_now = now.strftime("%A, %d %B, %Y at %X")

   return formatted_now


@app.route('/')

def welcomePage(): 
   return render_template('index.html', time = getTime())

@app.route('/menu.html')

def menu():
    return render_template('template1.html')

@app.route('/menu', methods=['GET','POST'])

def menu_post():
    return request.form('quantity1')

    
    

@app.route('/payment')

def payment():
    return render_template('payment.html')


@app.route('/cash')

def cash():
    return render_template('cash.html')

@app.route('/chef')

def chef():
    return render_template('CashierChef.html', pizzal = pizza)

# @app.route('/oven') 
# def oven(): 
 
#    board = CustomPymata4(baud_rate = 57600, com_port = "COM3")
#    number=10

#    while number >=0:
#       board.displayShow(number) 
#       timer=board.displayShow
#       time.sleep(1)
#       number -= 1
#       if number > 9999 :
#          number = 0

#       if (number > 0):
#          board.digital_write(4, 1)
#          board.digital_write(5, 0)
               
#       else:
#          board.digital_write(5, 1)
#          board.digital_write(4, 0)
      
#    return render_template('oven.html',)



if __name__ == "__main__":
    dbSetup()
    app.run()

