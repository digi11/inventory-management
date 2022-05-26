from datetime import datetime
from customer_side import application, orders_collection, shop_orders_collection, medicines_collection

from flask import session, redirect, request, render_template
import uuid, json
from firebase_admin import firestore


# this is an api to get 10 medicines from any shop at random
@application.route('/add-to-cart', methods=['POST','GET'])
def add_to_cart():
    if request.method == 'POST':
        try:  
            medicine = request.form
            data = {
                'name': medicine.get('name'),
                'price': medicine.get('price'),
                'desc': medicine.get('description'),
                'shop_address': medicine.get('shop_address'),
            }
            if 'cart' not in session:
                session['cart'] = []

            item = [ data['name'], data['desc'], data['price'], data['shop_address'] ]

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
            print('--------------GETTING CART--------------------')
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
            session['cart'].clear()
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
            print('---------------NEW ORDER ----------------')  
            print(session['cart'])
            count = 0
            order = dict()
            for i in session['cart']:
                order[str(count)] = {
                    'name': i[0],
                    'description': i[1],
                    'price': i[2],
                    'buyerid':session["uid"],
                    'quantity': request.form.get(i[0]),
                    'customer_address': session['user_address'],
                    'shop_address':i[3],
                    'buyer_address': session['user_address'],
                    'timestamp': datetime.now().strftime("%m/%d/%Y %H:%M:%S")
                }
                shop_orders_collection.document().set(order[str(count)])
                # medicines_collection.where(u'shop_address',u'==',order[str(count)]['shop_address']).where(u'name',u'==',order[str(count)]['name']).stream().update({"stock": firestore.Decrement(order[str(count)]['quantity'])})
                med = medicines_collection.where(u'shop_address',u'==',order[str(count)]['shop_address']).where(u'name',u'==',order[str(count)]['name']).get()
                inventory = dict()
                for doc in med:
                    # print(doc.to_dict())
                    inventory[doc.id] = doc.to_dict() 
                res = list(inventory.keys())[0]
                print(res)
                inventory[res]['stock'] = str(int(inventory[res]['stock']) - int(order[str(count)]['quantity']))
                medicines_collection.document(res).update({"stock": inventory[res]['stock']}) 
                    
                count = count + 1
            order['buyer_id'] = session['uid']
            order['buyer_address'] = session['user_address']
            order['timestamp'] = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            order_uid = uuid.uuid1().hex
            print(order_uid)
            json.loads(json.dumps(order))

            orders_collection.document(order_uid).set(json.loads(json.dumps(order)))
            session['cart'].clear()
            session.modified = True
            response = {
                "status": "Success",
                "type": "Order Placed Success",
                "msg": order
                }
            application.logger.info(response)
            return redirect('/get-orders')

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Order Placed Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)
