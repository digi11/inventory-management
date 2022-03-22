from customer_side import users_collection, orders_collection, medicines_collection, application

from flask import session, render_template,request



# this is an api to get all medicines from all the shops 
@application.route('/get-all-medicines', methods=['GET'])
def get_all_medicines():
    if request.method == 'POST':
        try:
            print(session['uid'])
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
            return response

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Get all medicine Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)


# this is an api to get 10 medicines from any shop at random
@application.route('/get-10-medicines', methods=['GET'])
def get_10_medicines():
    if request.method == 'POST':
        try:
            print(session['uid'])
            temp_inventory = medicines_collection.limit(10)
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