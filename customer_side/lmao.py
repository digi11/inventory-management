from customer_side import application

from flask import render_template
@application.route('/lmao', methods=['GET'])
def hell():
    application.logger.info("Inventory Management server running on localhost:7000")
    return render_template('base.html')
@application.route('/lmaoo', methods=['GET'])
def helll():
    application.logger.info("Inventory Management server running on localhost:7000")
    return "sex"