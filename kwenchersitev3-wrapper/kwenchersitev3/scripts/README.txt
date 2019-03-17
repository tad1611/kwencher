####copy and past into terminal
###sudo python __main__.py to run DB populate

sudo apt-get install python-mysqldb
sudo apt-get install libmysqlclient-dev
sudo apt-get install python-dev
pip install mysql-python
virtualenv dal_env
source dal_env/bin/activate
pip install django
pip install djangorestframework
cd dal_env
git clone https://kwencher:Shared1234@github.com/Kwencher/kwenchersitev2.git
cd kwenchersitev2/kwenchersitev2/
pip install -r scripts/requirements.txt
cd /dal_env/kwenchersitev2/kwenchersitev2/
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
# go to http://localhost:8000/admin/ and login
