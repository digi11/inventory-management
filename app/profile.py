from pkg_resources import register_namespace_handler
from app import application, shops_collection, users_collection

from flask import render_template, request, session



# api to update customer profile using UID as document id
@application.route('/update-customer-profile', methods=['POST'])
def update_customer_profile():
    if request.method == 'POST':
        try:
            result = request.form
            data = {
                "uid": result.get ('uid'),
                "email": result.get('email'),
                "name": result.get('name'),
                "contact": result.get('contact'),
                "address": result.get('address'),
            }
            print("Data => ")
            print(data)
            uid = result.get("uid")
            print("UID =>  " + uid)
            users_collection.document(uid).set(data)
            response = {
                "status": "Success",
                "type": "Update Profile Success",
                "msg": data
                }
            return response

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Update Profile Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template('error.html', error = response)

    if request.method == 'GET':
        profile = get_customer_profile(session['uid'])['msg']
        return render_template('update_profile.html', profile = profile)


# api to update admin profile using UID as document id
@application.route('/update-admin-profile', methods=['POST'])
def update_admin_profile():
    if request.method == 'POST':
        try:
            result = request.form
            data = {
                "uid": session['uid'],
                "email": result.get('email'),
                "name": result.get('name'),
                "contact": result.get('contact'),
                "address": result.get('address'),
            }
            print("Data => ")
            print(data)
            uid = result.get("uid")
            print("UID =>  " + uid)
            shops_collection.document(uid).set(data)
            response = {
                "status": "Success",
                "type": "Update Profile Success",
                "msg": data
                }
            return response

        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Update Profile Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template('error.html', error = response)

    if request.method == 'GET':
        profile = get_admin_profile(session['uid'])['msg']
        return render_template('update_profile.html', profile = profile)

# api to get the admin profile using UID as input 
@application.route('/admin-profile/<uid>', methods=['GET'])
def get_admin_profile(uid):
    if request.method == 'GET':
        try:
            profile = shops_collection.document(uid).get().to_dict()
            print(profile)
            response = {
              "status": "Success",
              "type": "Get Profile Success",
              "msg": profile  
            }
            return response
        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Get Profile Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template('error.html', error = response)



# api to get the vehicle profile using UID as input 
@application.route('/customer-profile/<uid>', methods=['GET'])
def get_customer_profile(uid):
    if request.method == 'GET':
        try:
            profile = shops_collection.document(uid).get().to_dict()
            print(profile)
            response = {
              "status": "Success",
              "type": "Get Profile Success",
              "msg": profile  
            }
            return response
        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Get Profile Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template('error.html', error = response)



@application.route('/admin-profile', methods=['GET'])
def admin_profile():
    if request.method == 'GET':
        profile = get_admin_profile(session['uid'])['msg']
        return render_template('profile.html', profile = profile)



@application.route('/customer-profile', methods=['GET'])
def customer_profile():
    if request.method == 'GET':
        profile = get_customer_profile(session['uid'])['msg']
        return render_template('profile.html', profile = profile)