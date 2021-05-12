from flask import Flask
from datetime import datetime

app = Flask(__name__)

wellcome = int(datetime.today().strftime("%H%M"))
message = ''
if wellcome < 1200:
    message = 'Bom dia!'
elif wellcome >= 1201 & wellcome < 1800:
    message = 'Boa tarde!'
else:
    message = 'Boa noite!'

x = datetime.today().strftime("%d/%m/%Y %H:%M:%S %p")
print(x)

@app.route('/current_datetime')
def datetime():
    return {'current_datetime': x,
    'message': message}


@app.route('/')
def hello_flask():
    return {'data': 'hello flask'}