from customer_side import users_collection, orders_collection, medicines_collection, application

from flask import session, render_template,request



# this is an api to get all medicines from all the shops 
@application.route('/get-all-medicines', methods=['GET'])
def get_all_medicines():
    if request.method == 'GET':
        try:
            # print(session['uid'])
            temp_inventory = medicines_collection.stream()
            inventory = dict()
            for doc in temp_inventory:
                # print(doc.to_dict())
                inventory[doc.id] = doc.to_dict() 

            print("Data => ")
            print(inventory)            

            response = {
                "status": "Success",
                "type": "Get all medicine Success",
                "msg": inventory
                }
            application.logger.info(response)
            return render_template('medicines.html', medicines=response['msg'])

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Get all medicine Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)


# this is an api to get 10 medicines from any shop at random
@application.route('/get-6-medicines', methods=['GET'])
def get_6_medicines():
    if request.method == 'GET':
        try:
            # print(session['uid'])
            temp_inventory = medicines_collection.limit(6).stream()
            print(temp_inventory)
            inventory = dict()
            for doc in temp_inventory:
                # print(doc.to_dict())
                inventory[doc.id] = doc.to_dict() 

            print("Data => ")
            print(inventory)            

            response = {
                "status": "Success",
                "type": "Get 10 medicine Success",
                "msg": inventory
                }
            application.logger.info(response)
            return response

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Get 10 medicine Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)


@application.route('/get-orders', methods=['GET'])
def get_medicine():
    if request.method == 'GET':
        try:
            
            print(session['uid'])
            temp_orders = orders_collection.where(u'buyerid',u'==',session['uid']).stream()
            orders = dict()
            for doc in temp_orders:
                # print(doc.to_dict())
                orders[doc.id] = doc.to_dict() 

            print("Data => ")
            print(orders)            

            response = {
                "status": "Success",
                "type": "Get Orders Success",
                "msg": orders
                }

            return render_template('orders.html' , orders = response['msg'])

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "get medicine Failed",
                "msg": e
                }
            return render_template("error.html", error = response)

@application.route('/tablets', methods=['GET'])
def tablets():
    if request.method == 'GET':
        try:
            
            tablets = medicines_collection.where(u'category',u'==',u'tablet').stream()
            print(tablets)
            inventory = dict()
            for doc in tablets:
                # print(doc.to_dict())
                inventory[doc.id] = doc.to_dict() 

            print("Data => ")
            print(inventory)            

            response = {
                "status": "Success",
                "type": "Get Tablets Success",
                "msg": inventory
                }

            return render_template('tablets.html' , tablet = response['msg'])

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "get tablets Failed",
                "msg": e
                }
            return render_template("error.html", error = response)


@application.route('/syrup', methods=['GET'])
def syrup():
    if request.method == 'GET':
        try:
               # print(session['uid'])
            syrup = medicines_collection.where(u'category',u'==',u'syrup').stream()
            print(syrup)
            inventory = dict()
            for doc in syrup:
                # print(doc.to_dict())
                inventory[doc.id] = doc.to_dict() 

            print("Data => ")
            print(inventory)            

            response = {
                "status": "Success",
                "type": "Get Tablets Success",
                "msg": inventory
                }

            return render_template('syrup.html' , syrup = response['msg'])

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "get tablets Failed",
                "msg": e
                }
            return render_template("error.html", error = response)


@application.route('/powder', methods=['GET'])
def powder():
    if request.method == 'GET':
        try:
            powder = medicines_collection.where(u'category',u'==',u'powder').stream()
            print(powder)
            inventory = dict()
            for doc in powder:
                # print(doc.to_dict())
                inventory[doc.id] = doc.to_dict() 

            print("Data => ")
            print(inventory)            

            response = {
                "status": "Success",
                "type": "Get Powder Success",
                "msg": inventory
                }

            return render_template('powder.html' , powder = response['msg'])

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "get Powder Failed",
                "msg": e
                }
            return render_template("error.html", error = response)
