from customer_side import application, database
from flask import render_template


# api for base route 
@application.route('/', methods=['GET'])
def hello():
    application.logger.info("Inventory Management customer side running on localhost:7001")
    return render_template('base.html')

# api for index page
@application.route('/index', methods=['GET'])
def index():
    medicines = database.get_6_medicines()
    print(medicines)
    
    application.logger.info("Index page loaded")
    return render_template('index.html', medicines = medicines['msg'])
