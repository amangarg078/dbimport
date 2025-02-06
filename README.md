
# Import a JSON file and provide APIs

This Django project imports a json file into a DB and provides CRUD APIs for the model.

# System Requirements
- Python >= 3.9
- Django >= 4.2

# Usage
To use this program, follow these steps:

1. Clone the repository to your local machine.

2. Setup a `.env` file in the root folder with the following values:
 - `SECRET_KEY`
 - `DB_NAME`
 - `DB_USER`
 - `DB_PASSWORD`
 - `DB_HOST`
 - `DB_PORT`

3. Run the migrations:
```
python manage.py migrate
```

4. Run the initial setup:
```
python manage.py initial-setup
```

5. You can run the tests:

```
python manage.py test dbimport.apps.api 
```

6. Run the server
```
python manage.py runserver 
```
