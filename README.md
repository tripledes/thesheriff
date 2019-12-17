# The Sheriff

[![Build Status](https://travis-ci.org/tripledes/thesheriff.svg?branch=master)](https://travis-ci.org/tripledes/thesheriff)

## Development

### Tools

* docker (docker-compose)
* Python 3.8
* pytest
* pipenv

### Python modules

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [SQLAlchemy Core](https://docs.sqlalchemy.org/en/13/core/)
* [Sphinx](https://pythonhosted.org/an_example_pypi_project/sphinx.html#full-code-example)

### Start the app

```console
$ docker-compose up
```

* Starts both services, *app* and *db*
* The *db* hostname can be used from the *app* for connecting to the database
* *app* is published on port *5000* in *localhost*
* Access it by `curl`:

```console
❯❯❯❯ curl localhost:5000
{"email":"guest@example.com","user":"guest"}
```

### Generate Documentation

* Documentation uses [Sphinx formatting](https://pythonhosted.org/an_example_pypi_project/sphinx.html)
* Take [AsaltoMySQLRespository](thesheriff/infrastructure/asalto/asalto_mysql_repository.py) as example
* If adding a new module, you'll need to add it to [index.rst](thesheriff/doc/index.rst) so it's added to the proper sections
* Generate new HTML contents
  ```console
  $ cd doc
  $ make html
  ```
  Open a web browser and point it to `file:///path/to/thesheriff/root/directory/doc/build/html/index.html`.