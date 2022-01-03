Recipe Manager
==============

Recipe manager in Python, using Django. This application is part of a test for Apicbase.

## Starting

### Prerequisites

Before starting, you will need to have the following tools installed on your machine:
* [Git](https://git-scm.com)
* [Python 3](https://www.python.org/)
* [PIP](https://pip.pypa.io/en/stable/)
<!-- * [Docker](https://www.docker.com/) -->
<!-- * [Docker Compose](https://docs.docker.com/compose/install/) -->

### Installation (Local Development)

```bash
# Clone this repository:
$ git clone https://github.com/rahenrique/rah.apicbase.test.git

# If necessary, run the following command to install virtualenv:
$ pip install virtualenv

# Run the following inside the root folder of the cloned repository, to create a virtual environment for the application:
$ python3 -m venv .venv

# After creating the environment, we need to activate it by running:
$ source .venv/bin/activate

# From this step beyond, all the commands are to be executed inside the virtual environment.
# You can confirm that you are running in the virtual environment looking for `(.venv)` at your terminal prompt. 
# Then, intall the dependencies:
(.venv)$ pip install -r src/requirements.txt

# To initialize the application, use the manage.py from Django:
(.venv)$ python3 manage.py runserver

# You should see something like the following on your terminal:
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

The Django embedded server will start on port:8000 in development mode. Any source code changes will automatically reflect in the running application.

Access:
* App: <http://127.0.0.1:8000/>
* Admin: <http://127.0.0.1:8000/admin>


### Pre-configured accounts
Default user access
username: rah
password: admin123456

Admin access
username: admin
password: admin123

