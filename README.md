# About the project
This is a project to practice Python Flask CRUD, testing, design patterns and clean code principles
# Preparing / Installing

### Clone the PythonCalculators repository
```
git clone https://github.com/claudiosw/Flask-CRUD-People.git
```

### Access the project directory:
```
cd Flask-CRUD-People
```

### Create the virtual environment:
```
python -m venv venv

```

### Run the virtual environment:
```
venv\Scripts\activate

```

### Install the required Python packages:
```
pip install -r requirements.txt
pre-commit install
```

### Create the database and the database structure:
```
python
>>> from src.models.config import *
>>> from src.models.entities import *
>>> db_conn = DBConnectionHandler()
>>> engine = db_conn.get_engine()
>>> Base.metadata.create_all(engine)
```

### Run Flask:
```
set FLASK_APP=run
python -m flask run
```

### Create person
Do a POST to the url http://127.0.0.1:5000/person

With this data in the body (you can change the values):
```
{"name": "Claudio", "neighbourhood": "Jd Planalto", "age": 43, "profession": "Developer"}
```

### Retrieve person
Do a GET to the url http://127.0.0.1:5000/person

With parameter name=Claudio (you can change the values):
