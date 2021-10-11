# SARTHI_AI_PROJECT
# SARTHI_AI-PROJECT
## Ice and Fire API (Django Rest Framework)
This project uses Ice and Fire API to get books. It also provides CRUD operations for books.

### Setup virtual environment for project

virtualenv -p python3 ice-and-fire
source ice-and-fire/bin/activate
pip install -r requirements.txt


### Run database migrations 

python manage.py makemigrations
python manage.py migrate


### Run tests

python manage.py test


### Run server

python manage.py runserver
