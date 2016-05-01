**Product Price**
>Display product price on daily basis.(only APIs included)

**Installation:**

- setup the repo and install required modules from requirements.txt
```
git clone https://github.com/radhika19/Product_Price.git
cd Product_Price
```
when using virtualenv 
```
virtualenv .
. bin/activate
pip install -r requirements.txt
```
- to create an mysql server:
```
sudo apt-get install mysql-server
```
- the mysql database settings have been added in settings.py file. make changes w.r.t **user** and **password**
```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': Inventory,
    'USER': <username>,
    'PASSWORD': <password>,
    'HOST': 'localhost',
    }
}
```
- migrate the models:
```
cd price
python manage.py makemigrations price_App
python manage.py migrate
```
- install redis-server
```
http://redis.io/topics/quickstart
```
(used redis here to access the prices on a daily basis from the redis-datastore instead of hitting the database.
 but have to be careful with memory consumption.)
- start the server
```
python manage.py runserver
```
- Note:To create the username/password for admin page.
  can add the products from here.
```
python manage.py createsuperuser
 ```
**API Reference:**

The APIs are documented with examples: [API document](https://github.com/radhika19/Product_Price/blob/master/apiary.apib)
