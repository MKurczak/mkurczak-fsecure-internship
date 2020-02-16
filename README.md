# Marek Kurczak F-Secure internship exercise.

## Getting Started

This project is for F-Secure company intenrnship program. Its based on Python, Django, Docker, Docker-compose and Postgres.
No additional frameworks were used here.
Instructions below will explain how to install/run and test the application.

### Prerequisites

What things you need to install the software and how to install them

```
Docker version 19.03.6
docker-compose version 1.24.1
```
To install this components execute command below
```
sudo <package manager command> docker docker-compose
```
Package manager command will be different for some Linux distributions eg:
For Fedora/CentOs
``` 
sudo yum install docker docker-compose
```
For Ubuntu
```
sudo apt-get install docker docker-compose
```
If for any reason specific version of Docker is needed please add Docker repository to package manager
- for Fedora: https://docs.docker.com/install/linux/docker-ce/fedora/
- for Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/
Site above also have tutorials for CentOs and Debian.

### Installation

Instructions how to install application.

Use CLI to clone repository
```
git clone git@github.com:MKurczak/mkurczak-fsecure-internship.git
```
Or use any software that suits Your needs
```
git@github.com:MKurczak/mkurczak-fsecure-internship.git
```

### Starting the app

To start the application follow this steps
Use docker-compose to start
```
<Get into cloned git repository folder>
docker-compose up --build (add --detach if CLI output is not necessary)
```
or use bash script provided within repository
```
<Get into cloned git repository folder>
./run.sh
```
here is list of avialable arguments that can be used with script
```
./run.sh usage:
        f) # Build and run
        b) # Build docker-compose.
        u) # Start docker-compose.
        s) # Stop docker-compose if running
        r) # Restart docker-compose
        d) # Build and run detached docker-compose
        h) # Help.
```
# Note: Application will use port 8000 by default

### Testing

## System check
If steps above was reproduced sucessfully this output should appear in CLI if detached option wasn't used
```
web_1  | System check identified no issues (0 silenced).
web_1  | February 16, 2020 - 16:01:09
web_1  | Django version 3.0.3, using settings 'awsExcerciseProject.settings'
web_1  | Starting development server at http://0.0.0.0:8000/
web_1  | Quit the server with CONTROL-C.
```
if detached option was selected, steps to check if application is running correctly
```
docker ps
```
and this should be output from docker
```
CONTAINER ID        IMAGE                             COMMAND                  CREATED              STATUS              PORTS                    NAMES
8b743998b5b6        mkurczak-fsecure-internship_web   "bash -c 'python app…"   About a minute ago   Up 58 seconds       0.0.0.0:8000->8000/tcp   mkurczak-fsecure-internship_web_1
1e7b91affc67        postgres                          "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp                 mkurczak-fsecure-internsh
```
## App testing
Steps to test application functionalities:
# Depending on system settings there might be need to test two IP's: 127.0.0.1 & 0.0.0.0 both with port 8000 which is set as default for app.
Accessing URL without any "/site" will result in default Django error page with listed URL's that are available.
- Random - <host>:<port>/random (GET) - accessing this should return JSON with "status" and "random generated" number
  Two options to test this feature
  ```
  Use browser and go under this url
  http://127.0.0.1:8000/random 
  or 
  http//0.0.0.0:8000/random
  ```
  or use console
  ```
  curl http://127.0.0.1:8000/random
  curl http://0.0.0.0:8000/random
  ```
- Echo - <host>:<port>/echo (POST) - accessing (GET) this page should return warning that POST method should be used
  Expeced output should be status and POST'ed message in JSON format. Also each time this functionality is invoked it will create entry in database.
  To test this use CLI
  ```
  curl -d '<message>' http://127.0.0.1:8000/echo
  or
  curl -d '<message>' http://0.0.0.0:8000/echo
  ```
  Note: Echo feature will accept only valid JSON as message otherwise it will return status: "error" and "error message" in JSON format, Echo response does not affect creating database record.
- List - <host>:<port>/list - accessing this page should return records from database. This is basic output without any styling added. If database is empty (Echo functionality wasn't used) it will return blank page otherwise it will return database records.
  To test this use CLI and browser
  ```
  First use: 
  curl -d '<message>' http://127.0.0.1:8000/echo
  or
  curl -d '<message>' http://0.0.0.0:8000/echo
  
  then go to this URL
  http://127.0.0.1:8000/list
  or
  http://0.0.0.0:8000/list
  ```
  If everything was executed correctly instead of blank page there should be JSON like format (querySet) with database ID and records.
### Project directory structure

  - application - root folder that holds Django project
    - app - Django app
    - awsExcerciseProject - Django project settings
    
Where to look for each functionality code?
```
application/app/views/*.py
```
This location got all page views used "echo/random/list"
Where to look for database model?
```
application/app/models.py
```
Where to look for urls settings?
```
application/app/urls.py
```

### Author

* **Marek Kurczak** - marekekurczak@gmail.com
