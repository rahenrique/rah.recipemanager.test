Recipe Manager
==============

Recipe manager in Python, using Django. This codebase was used as an application test.

## Starting

### Prerequisites

Before starting, you will need to have the following tools installed on your machine:
* [Git](https://git-scm.com)
* [Python 3](https://www.python.org/)
* [pyenv](https://github.com/pyenv/pyenv)
* [Poetry](https://python-poetry.org/)

### Installation (Local Development)

```bash
# Clone this repository:
$ git clone https://github.com/rahenrique/rah.recipemanager.test.git

# Install Python v3.10 with pyenv:
$ pyenv install 3.10.0

# Run the following inside the root folder of the cloned repository, to create a virtual environment for the application:
$ pyenv virtualenv 3.10.0 rah.recipemanager

# After creating the virtual environment, we need to define it as the local virtualenv
# This ensures the virtualenv is automatically activated on entering the project folder:
$ pyenv local rah.recipemanager

# Let's create a symlink for the virtuanenv:
# (It's necessary so Poetry can use this virtualenv easily)
$ ln -s ~/.pyenv/versions/rah.recipemanager/ ./.venv

# Configure Poetry to not create a new virtualenv, using the local virtualenv instead:
$ poetry config virtualenvs.create false
$ poetry config virtualenvs.in-project true

# Install all dependencies:
$ poetry install

# To initialize the application, use the manage.py from Django:
(.venv)$ python3 recipe_manager/manage.py runserver

# You should see something like the following on your terminal:
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The Django embedded server will start on port:8000 in development mode. Any source code changes will automatically reflect in the running application.

Access:
* App: <http://127.0.0.1:8000/>
* Admin: <http://127.0.0.1:8000/admin>

## Initial database seed

For simplicity, there is no need for apply a initial database seed. The `db.sqlite3` file shipped within the repository has all the necessary data for a initial testof the features of the application.

## Pre-configured accounts
**Default user access**  
username: `rah`  
password: `admin123456`  

**Admin access**  
username: `admin`  
password: `admin123`  

## Running tests
To run the unit tests provided with the application, run the following command on the virtual environment terminal:

```bash
# This will run all tests inside the Django apps
(.venv)$ python3 recipe_manager/manage.py test recipe_manager/ --verbosity=2
```
