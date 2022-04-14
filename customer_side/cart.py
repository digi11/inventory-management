from customer_side import application, cart_collection

from flask import session, redirect, request, render_template



# this is an api to get 10 medicines from any shop at random
@application.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    if request.method == 'POST':
        try:  
            medicine = request.form.get('data')
            data = {
                'medicine': medicine
            }
            if 'cart' not in session:
                session['cart'] = []

            item = [ request.form['product_name'], request.form['product_description'], request.form['price'] ]

            if item:
                session['cart'].append(item)
            session.modified = True
            response = {
                "status": "Success",
                "type": "Add to cart Success",
                "msg": data
                }
            application.logger.info(response)
            return response

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Add to cart Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)


