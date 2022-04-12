from cgitb import text
import csv
from distutils.log import debug
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
    f = open('data.csv', 'a')
    writer = csv.writer(f)
    total = 0 
    writer.writerow(["---------------------------------------------" + getTime()])
    if str(request.form['quantity1']) != '0':
        data = int(request.form['quantity1'])
        price = data * 5
        row= ('Margherita   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])

    if str(request.form['quantity2']) != '0':
        data = int(request.form['quantity2'])
        price = data * 7
        row= ('Salami   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
        
    if str(request.form['quantity3']) != '0':
        data = int(request.form['quantity3'])
        price = data * 7.50
        row= ('BBQChicken   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
       

    if str(request.form['quantity4']) != '0' :
        data = int(request.form['quantity4'])
        price = data * 6.50
        row= ('4Cheese   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
   

    if str(request.form['quantity5']) != '0':
        data = int(request.form['quantity5'])
        price = data * 5.50
        row= ('Doner   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
    
    if str(request.form['quantity6']) != '0':
        data = int(request.form['quantity6'])
        price = data * 5
        row= ('Veggie   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
   
    if str(request.form['quantity7']) != '0':
        data = int(request.form['quantity7'])
        price = data * 7.50
        row= ('Hawaiian   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])


    if str(request.form['quantity8']) != '0':
        data = int(request.form['quantity8'])
        price = data * 7
        row= ('BBQ   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])


    if str(request.form['quantity9']) != '0':
        data = int(request.form['quantity9'])
        price = data * 5.50
        row= ('Chocolate   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])

    if str(request.form['quantity10']) != '0':
        data = int(request.form['quantity10'])
        price = data * 6.50
        row= ('Spaghetti Bolognaise   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
   
    if str(request.form['quantity11']) != '0':
        data = int(request.form['quantity11'])
        price = data * 5.50
        row= ('Spaghetti Carbonara   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])

    if str(request.form['quantity12']) != '0':
        data = int(request.form['quantity12'])
        price = data * 6
        row= ('Mac&Cheese   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
    

    if str(request.form['quantity13']) != '0':
        data = int(request.form['quantity13'])
        price = data * 2.50
        row= ('Cola   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])

    
    if str(request.form['quantity14']) != '0':
        data = int(request.form['quantity14'])
        price = data * 3
        row= ('Red Bull   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
    

    if str(request.form['quantity15']) != '0':
        data = int(request.form['quantity15'])
        price = data * 2
        row= ('Spa Intense   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
    

    if str(request.form['quantity16']) != '0':
        data = int(request.form['quantity16'])
        price = data * 2.50
        row= ('Sprite   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
    
    if str(request.form['quantity17']) != '0':
        data = int(request.form['quantity17'])
        price = data * 4
        row= ('Jupiler   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])

    if str(request.form['quantity18']) != '0':
        data = int(request.form['quantity18'])
        price = data * 2.50
        row= ('Fanta   ' +  str(data) + '   ' + '\u20ac' + str(price) )
        total = total + price
        writer.writerow([row])
    

    writer.writerow(['With the total of ' + '\u20ac' + str(total)])
    return ''

    
    

@app.route('/payment')

def payment():
    return render_template('payment.html')


@app.route('/cash')

def cash():
    return render_template('cash.html')

@app.route('/chef')

def chef():
    file = open('data.csv')
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
            rows.append(row)
    
    
    return render_template('CashierChef.html', pizzal = rows)

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
    app.config['DEBUG'] = True
    app.run(host='145.93.73.178', port='5000', debug=True)

