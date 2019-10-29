# global-companies-portal (v.0)
This is a global company portal using RDF implementation

## Requirements
Please download these first before reading the instruction part.
- Git
- Python (this project uses Python 2.7)
- MySQL
- The modules 

## Instruction
1. After cloning this project, please run this command below on your cmd to automatically install the modules needed for developing this project.
```
pip install -r requirements.txt
```
2. Don't change the name of any folder. Please run the following command on your cmd after successfully installed module in requirements.txt to activate virtual environment for django.
```
venv\Scripts\activate
```
In git bash, you can use the following command.
```
source venv/Scripts/activate
```

3. Please run the following command to see the project development.
```
python2 manage.py runserver
```
* In git bash, there will be no output. You can just open the link shown in step 4.

4. Once, you run the previous command, you would see output as shown below on your cmd.
```
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
October 26, 2019 - 00:00:41
Django version 1.11.25, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK
```
This project can be seen through the link shown on cmd as development server (http://127.0.0.1:8000/).

*References:* 

- [https://realpython.com/django-setup/](https://realpython.com/django-setup/)
- [https://docs.djangoproject.com/en/1.7/intro/tutorial01/](https://docs.djangoproject.com/en/1.7/intro/tutorial01/)
