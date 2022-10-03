# Mailing
### Description 
Mailing with external API. Messages are sent to сlients with a specific tag and mobile code.

There are three instances:
# Mailing
Attributes:
```
- unique id;
- time and date of the start;
- text message;
- filter (tag or mobile code);
- time and date of the end.
```

# Client
Attributes:
```
- unique id;
- phone number in 7XXXXXXXXXX format;
- mobile code;
- tag;
- timezone.
```

# Message
Attributes:
```
- unique id;
- sending time and date;
- status;
- mailing id;
- client id.
```

# You can:
```
- add new clients;
- update clients;
- delete clients;
- add new mailings;
- get statistics for mailings;
- update mailings;
- delete mailings;
- send messages.
```

If the request failed, it will be postponed.

### Getting started

Install and run Redis:

```
sudo apt-get update
sudo apt-get install redis
sudo service redis-server start
```

Clone this repository, create file '.env' in the project directory with variables:

```
TOKEN='<your API token>'
URL='<API URL>'
SECRET_KEY='<django_sekret_key>'
```
Create and activate virtual environment:

```
py -3.10 -m venv venv
source venv/Scripts/activate
```

Install required packages from req.pip:

```
pip install -r req.pip
```

Apply migrations:

```
py manage.py migrate
```

Create a superuser:

```
py manage.py createsuperuser
```

Run the project:

```
py manage.py runserver
```

Run Celery. for example (Windows):

```
celery -A mailing worker --loglevel=info --pool=solo
```
Run Flower:

```
celery -A mailing flower --port=5555
```

Project URL:

```
http://127.0.0.1:8000/
```

Admin panel URL:

```
http://127.0.0.1:8000/admin
```

API documentation:

```
http://127.0.0.1:8000/swagger/
```

Create clients and mailings (Postman or Admin panel).
You can see satus of mailings via Flower (http://127.0.0.1:5555/), Postman (see API documentation http://127.0.0.1:8000/swagger/) or admin panel.


### Tech stack

Python 3.10, Django, DRF, Celery, Redis, Swagger, Flower, dotenv

### Author

Nikita Burtsev (https://t.me/telekasster)
