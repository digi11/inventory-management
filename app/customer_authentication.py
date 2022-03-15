from logging import exception
from app import application, auth


from flask import request, session, render_template


# api to facilitate application login for a customer 
@application.route("/customer-login", methods=['GET','POST'])
def customer_login():
    if request.method == 'POST':
        try: 
            data = request.form
            email = data.get('email')
            password = data.get('password')

            user = auth.sign_in_with_email_and_password(email, password)

            uid = user['localId']
            session['uid'] = uid #used to create a session

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
            return render_template("error.html", error = response)
    if request.method == "GET":
        return render_template("customer-login.html")


# api to facilitate change password functionality for a user
@application.route("/changepwd", methods=['POST'])
def change_password():
    if request.method == 'POST':
        try: 
            data = request.form
            email = data.get('email')
            auth.send_password_reset_email(email)
            response = {
                "status": "Success",
                "type": "Password Change Success",
                "msg": "password reset email sent"
                }
            return response
        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Password Reset Failed",
                "msg": e
                }
            return response


# api to facilitate registration of a new customer on the application
@application.route('/customer-register', methods=['POST'])
def customer_register():
    if request.method == 'POST':
        try: 
            data = request.form
            email = data.get('email')
            password = data.get('password')
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