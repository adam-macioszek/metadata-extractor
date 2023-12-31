# metadata-extractor

### Setup
Assuming you have python3 and pip installed, you should get up a virtualenv for this project. If you don't have a preferred way to set that up run the following commands from the root directory of this project: 
```
python3 -m venv ./.venv/djangodev

source ./.venv/djangodev/bin/activate

pip install -r requirements.txt
```

This will install Django and sqlalchemy in a local venv.

Once you have everything set up locally run:
```
python manage.py runserver
```
from metadata-extractor/metadb to start the django server locally on port 8000. To customize the port simply include the new port at the end of the previous command.

To get the metadata From a database please send a get request with a URL Encoded database connection string at whatever port on localhost you spun up the server on.

```
http://localhost:8000/metadata/postgresql%3A%2F%2Fpostgres%3Secretb%40HOSTNAME%3A5432%2FDBNAME%3Fsslmode%3Ddisable
```
 It should return a list of the following objects mapping to your Database:
 ```
     {
        "columns": [
            {
                "col_name": "",
                "col_type": ""
            },
        ],
        "name": "",
        "num_rows": "",
        "database": "",
        "schema": ""
    },
 ```
 One thing I wasn't sure of was what the schema field meant, none of the databases I tried had a value for the field table.schema, but I believe with clarification I could fill that out.
