# CommodityPedia
(*This is an old project and it may need some changes!*)
This is a social media app based on django! 

How to run: 
``` bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
cd commoditypedia
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver 8080
```
Now it's on localhost:8080

Now you can log in to admin panel in [localhost:8080/admin](http://127.0.0.1:8080/admin) 

