# pdf_xml_service
This includes my application of flask microservice which generates pdf or xml documents according to given schema

# Setup
To run the project pelase set up a virtual enviroment. Make sure that you have python3 version >= 3.6 .

First lets create one:
```bash
python3 -m venv Env
```
Don't forget to activate it:
```bash
source Env/bin/activate
```
Then install all of the required packages:
```bash
pip install -r requirements.txt
```

Now, all that is left before running is to set up server credentials in you local machine.
```bash
export DATABASE_URL="<database_url>"
export DATABASE_PW="<database_password>"
export DATABASE_DB="<database_name>"
export DATABASE_USER="<database_user>"
```
These will then form full database url in a form 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'

# Runing the service

Once you have the eviroment set up it's time to try out the project.
You can get Flask server running localy:
```bash
python service.py
```
exaple query (if it is running on local mashine and is on port 5000) can look like:
http://127.0.0.1:5000/generate-report?type=xml&id=1
