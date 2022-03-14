from app import application, auth


from flask import Flask, request, session


# api to facilitate application login for a shop
@application.route("/admin-login", methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        try: 
            data = request.form
            email = data.get('email')
            password = data.get('password')

            user = auth.sign_in_with_email_and_password(email, password)

            uid = user['localId']
            session['uid'] = uid
            response = {
                "status": "Success",
                "type": "Login Success",
                "msg": uid
                }
            return response
            
        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Login Failed",
                "msg": e
                }
            return response



# api to facilitate registration of a new shop on the application
@application.route('/admin-register', methods=['POST'])
def admin_register():
    if request.method == 'POST':
        try: 
            data = request.form
            email = data.get('email')
            password = data.get('pwd')
            print(email)
            user = auth.create_user_with_email_and_password(email, password)
            user_details = auth.get_account_info(user['idToken'])
            uid = auth.refresh(user['refreshToken'])  

            session['uid'] = uid
            response = {
                "status": "Success",
                "type": "Register Success",
                "msg": uid
                }
            return response

            
        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Register Failed",
                "msg": e
                }
            return response