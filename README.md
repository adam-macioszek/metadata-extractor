# metadata-extractor

###Setup
Assuming you have python3 and pip install, you should get up a virtualenv for this project. If don't have a prefered way to set that up run the following commands from the root directory of this project: 
```
python3 -m venv ./.venv/djangodev

source ./.venv/djangodev/bin/activate

pip install -r requirements.txt
```

This will install django and sqlalchemy in a local venv.

Once you have everything setup locally run:
```
python manage.py runserver
```
from metadata-extractor/metadb to start the django server locally on port 8000. To customize the port simply include the new port at the end of the previous command.
