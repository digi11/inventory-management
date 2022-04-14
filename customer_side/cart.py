from customer_side import application, cart_collection

from flask import session, redirect, request, render_template



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