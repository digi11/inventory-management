from customer_side import application, orders_collection

from flask import session, redirect, request, render_template
import uuid



# this is an api to get 10 medicines from any shop at random
@application.route('/add-to-cart', methods=['POST','GET'])
def add_to_cart():
    if request.method == 'POST':
        try:  
            medicine = request.form
            data = {
                'name': medicine.get('name'),
                'price': medicine.get('price'),
                'desc': medicine.get('description')
            }
            if 'cart' not in session:
                session['cart'] = []

            item = [ data['name'], data['desc'], data['price'] ]

            if item:
                session['cart'].append(item)
            session.modified = True
            response = {
                "status": "Success",
                "type": "Add to cart Success",
                "msg": data
                }
            application.logger.info(response)
            return redirect('/index')

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Add to cart Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)

    if request.method == 'GET':
        try:  
            print(session['cart'])
            data = session['cart']
            response = {
                "status": "Success",
                "type": "Get cart Success",
                "msg": data
                }
            application.logger.info(response)
            return render_template('cart.html', cart = response['msg'])

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Get cart Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)

# this is an api to clear the current cart
@application.route('/clear-cart', methods=['POST','GET'])
def clear_cart():
    if request.method == 'POST':
        try:  
            session['cart'].pop()
            session.modified = True
            response = {
                "status": "Success",
                "type": "Clear cart Success",
                "msg": session
                }
            application.logger.info(response)
            return redirect('/index')

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Clear cart Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)


# this is an api to place an order 
@application.route('/new-order', methods=['POST','GET'])
def new_order():
    if request.method == 'POST':
        try:  
            print(session['cart'])
            count = 0
            order = dict()
            for i in session:
                order[count] = {
                    'name': i[0],
                    'price': i[1],
                    'description': i[2],
                    'buyerid':session["uid"]
                }
                count = count + 1
            orders_collection.document(uuid.uuid1().hex).set(order)
            session['cart'].pop()
            session.modified = True
            response = {
                "status": "Success",
                "type": "Order Placed Success",
                "msg": order
                }
            application.logger.info(response)
            return render_template('orders.html')

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Order Placed Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)



@application.route('/orderfin', methods=['POST','GET'])
def finorder():
    if request.method == 'POST':
        try:  
            application.logger.info(response)
            return render_template('orderfin.html')

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Order Placed Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)