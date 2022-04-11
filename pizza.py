from flask import *
from datetime import *
from time import *
from pymysql import *

app = Flask(__name__, template_folder='templates')


def dbSetup(host, user, pwd, db):
    cursor = connect(host, user, pwd, db).cursor()
    cursor.execute('''CREATE TABLE [IF NOT EXISTS] pizzashop( 
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

@app.route('/order', methods=['GET','POST'])



@app.route('/menu', methods=['GET','POST'])

def menu():
    def getData():
        i = 0
        a = []
        while i < 18:
            price = request.form['quantity'+str(i)]
            a.append(price)
            i = i + 1
        return render_template('template1.html',value = i)

@app.route('/payment')

def payment():
    return render_template('payment.html')

@app.route('/cash')

def cash():
    return render_template('cash.html')

@app.route('/chef')

def chef():
    return render_template('CashierChef.html')

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
    dbSetup("localhost","testuser","test123","TESTDB" )
    app.run()
