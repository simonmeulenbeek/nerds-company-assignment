# Nerds & Company - job-application assignment

## About

An unfinished OAuth2 authentication server implementation. 


## Dependencies

This app depends on
* Flask
* PyTest
* PyTest-Flask

Install the required dependencies with pip by specifying the directory containing `setup.py`:
```shell
$ pip install -e .
```


## Running

```shell
$ export FLASK_APP=auth_server
$ export FLASK_ENV=development
$ flask run
```

## Testing
The tests are implemented with PyTest. To run the tests:
```shell
$ python -m pytest tests
```