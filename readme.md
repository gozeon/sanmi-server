# run 
```
FLASK_APP=main FLASK_ENV=development flask run
```

# db

```
FLASK_APP=main flask db init
FLASK_APP=main flask db migrate -m "Initial migration."
FLASK_APP=main flask db upgrade
```

# create admin

```
FLASK_APP=main flask create-admin
```
