from app import application, medicines_collection, shop_orders_collection

from flask import redirect, render_template, request, session

@application.route('/add-medicine', methods=['GET','POST'])
def add_medicine():
    if request.method == 'GET':
        return render_template ('add_medicine.html')
    
    if request.method == 'POST':
        try:
            
            print(session['uid'])
            result = request.form
            data = {
                "name": result.get ('name'),
                "stock": result.get('stock'),
                "description": result.get('description',""),
                "shopid": session['uid'],
                "price": result.get('price'),
                "shop_address": session['shop_address'],
                "category": result.get('category')

            }
            print("Data => ")
            print(data)            

            medicines_collection.document().set(data)
            response = {
                "status": "Success",
                "type": "Add medicine Success",
                "msg": data
                }

            return redirect('/dashboard')

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Add medicine Failed",
                "msg": e
                }
            return render_template("error.html", error = response)

@application.route('/delete-medicine/<med_id>', methods=['POST'])
def delete_medicine(med_id):    
    if request.method == 'POST':
        try:
            
            print(session['uid'])
            medicine_uid = med_id          

            medicines_collection.document(medicine_uid).delete()
            response = {
                "status": "Success",
                "type": "Delete medicine Success",
                "msg": medicine_uid
                }

            return redirect('/dashboard')

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Delete medicine Failed",
                "msg": e
                }
            return render_template("error.html", error = response)


@application.route('/get-medicine', methods=['GET'])
def get_medicine():
    if request.method == 'GET':
        try:
            
            print(session['uid'])
            temp_inventory = medicines_collection.where(u'shopid',u'==',session['uid']).stream()
            inventory = dict()
            for doc in temp_inventory:
                # print(doc.to_dict())
                inventory[doc.id] = doc.to_dict() 

            print("Data => ")
            print(inventory)            

            response = {
                "status": "Success",
                "type": "Add medicine Success",
                "msg": inventory
                }

            return response

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "get medicine Failed",
                "msg": e
                }
            return render_template("error.html", error = response)


@application.route('/get-medicine/<med_uid>', methods=['GET'])
def get_one_medicine(med_uid):
    if request.method == 'GET':
        try:
            
            print(session['uid'])
            temp_inventory = medicines_collection.document(med_uid).get()
            print(temp_inventory)
            inventory =temp_inventory.to_dict()
            print("Data => ")
            print(inventory)            

            response = {
                "status": "Success",
                "type": "Add medicine Success",
                "msg": inventory,
                "med_uid": med_uid
                }

            return render_template('update_medicine.html', medicine = response['msg'], med_uid = response['med_uid'])

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "get medicine Failed",
                "msg": e
                }
            return render_template("error.html", error = response)

@application.route('/update-medicine/<med_uid>', methods=['POST'])
def update_medicine(med_uid):
    if request.method == 'POST':
        try:
            
            print(session['uid'])
            result = request.form
            data = {
                "name": result.get ('name'),
                "stock": result.get('stock'),
                "description": result.get('description',""),
                "shopid": session['uid'],
                "price": result.get('price'),
                "shop_address": session['shop_address'],
                "category": result.get('category')



            }
            print("Data => ")
            print(data)            

            medicines_collection.document(med_uid).set(data)
            
            response = {
                "status": "Success",
                "type": "Update medicine Success",
                "msg": med_uid
                }

            return redirect('/dashboard')

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Update medicine Failed",
                "msg": e
                }
            return render_template("error.html", error = response)

@application.route('/get-orders', methods=['GET'])
def get_orders():
    if request.method == 'GET':
        try:
            
            print(session['uid'])
            temp_inventory = shop_orders_collection.where(u'shop_address',u'==',session['shop_address']).stream()
            inventory = dict()
            for doc in temp_inventory:
                # print(doc.to_dict())
                inventory[doc.id] = doc.to_dict() 

            print("Data => ")
            print(inventory)            

            response = {
                "status": "Success",
                "type": "get orders Success",
                "msg": inventory
                }

            return render_template('orders.html', orders=response['msg'])
            # return response

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "get medicine Failed",
                "msg": e
                }
            return render_template("error.html", error = response)