# INVENTORY MANAGEMENT SYSTEM 🗃️
---

## Pre-requistes
<br>

1. Python **3.7** >
2. Pip3 

---

## Setup

<br>

Cloning the repositry
<br>

```
git clone https://github.com/digi11/inventory-management.git
```
<br>

Adding the **Config** Files
> 1. Create a Firebase project and add the app to your project 
> 2. Copy the config json and paste it in a file named config.py in directory /app/config.py
> 3. Create a JSON key for the firebase admin serice account from the GCP Console of your Firebase project
> 4. Download the JSON key
> 5. Rename the JSON Key File as firestore_config.json
> 6. Move firestore_config.json in the directory /app/firestore_config.json 

<br>

Installing the dependencies

```
pip install -r requirements.txt
```
<br>

Running the **ADMIN Server**

```
python application.py
```
<br>

To check if admin application is running open http://localhost:7000
> response should be
> "Inventory management server is running" 

<br>

Running the **Customer Side Server**

```
python customer_app.py
```
<br>

To check if customer side application is running open http://localhost:7001
> response should be
> "Inventory management server is running" 

---

<br>

**NOTE**
1. "templates" folder stores the html files
2. "static" folder stores the css and .js files
3. "app" folder stores the APIs
