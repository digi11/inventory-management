from app import application

# api for base route 
@application.route('/', methods=['GET'])
def hello():
    return "Inventory Management server running on localhost:7000"
