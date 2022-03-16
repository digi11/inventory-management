from customer_side import application
from flask import render_template


# api for base route 
@application.route('/', methods=['GET'])
def hello():
    application.logger.info("Inventory Management server running on localhost:7000")
    return render_template('base.html')
