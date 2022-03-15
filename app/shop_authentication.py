from app import application, auth, shops_collection


from flask import redirect, render_template, request, session



# api to facilitate application login for a shop
@application.route("/admin-login", methods=['GET','POST'])
def admin_login():
    if request.method == 'POST':
        try: 
            data = request.form
            email = data.get('email')
            password = data.get('password')

            user = auth.sign_in_with_email_and_password(email, password) # sign in using firebase

            uid = user['localId']
            session['uid'] = uid # create session for the user on the flask server
            response = {
                "status": "Success",
                "type": "Login Success",
                "msg": uid
                }
            application.logger.info(response)
            return redirect('/dashboard')
            
        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Login Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template("error.html", error = response)

    if request.method == "GET":
        return render_template("admin-login.html")



# api to facilitate registration of a new shop on the application
@application.route('/admin-register', methods=['POST','GET'])
def admin_register():
    if request.method == 'POST':
        try: 
            result = request.form
            email = result.get('email')
            password = result.get('password')
            print(email)
            user = auth.create_user_with_email_and_password(email, password) # create user on firebase
            user_details = auth.get_account_info(user['idToken'])
            uid = auth.refresh(user['refreshToken'])['userId'] # get user's unique id

            session['uid'] = uid
            response = {
                "status": "Success",
                "type": "Register Success",
                "msg": uid
                }


            # add data to shops firestore collection 
            data = {
                "uid": uid,
                "email": result.get('email'),
                "name": result.get('name'),
                "address": result.get('address'),
                "phone": result.get('phone'),
            }
            print("Data => ")
            print(data)
            print("UID =>  " + uid)
            shops_collection.document(uid).set(data)

            application.logger.info(response)
            return redirect('/dashboard')

            
        except Exception as e:
            response = {
                "status": "Failed",
                "type": "Register Failed",
                "msg": e
                }
            application.logger.error(response)
            return render_template('error.html', error= response['msg'])

    if request.method == 'GET':
        return render_template('registration_form.html')

@application.route('/logout')
def logout():

    session.pop ('uid',None) #terminate the session on flask side
    
    auth.current_user = None # set the current user to none on the firebase side

    return redirect('/')