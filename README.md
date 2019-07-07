# Django-mongo_integration
There is the sample of integration between Mongodb and Django framework that will be develop and will be implement more features
## Getting Started

In the toplevel directory of the project there is a requirements.txt file with all the python dependencies, required for this project to run. Install them with

```
pip install -r requirements.txt
```

To run this project with django development server, just go to project folder and say:

```
 python manage.py runserver
 ```


and visit http://localhost:8000/api/ url, where you'll find the root of your REST api.

# Project structure

The toplevel directory contains a single django project
, Within it there are a per-project folder called project, where global settings are stored, and one django app, djanog_app.
  app contains several API endpoints and demonstrating DRF-Mongoengine capabilities for storing as ODM.