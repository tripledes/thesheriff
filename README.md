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
$ make run
```

* Starts both services, *app* and *db*
* The *db* hostname can be used from the *app* for connecting to the database
* *app* is published on port *5000* in *localhost*
* Access it by `curl`:

```console
$ curl localhost:5000/api/v1/outlaw/ -X POST --data @examples/json/create_outlaw.json -H 'Content-Type: application/json'
{"message":"Outlaw added successfully","status":201}
```

### Generate Documentation

* Documentation uses [Sphinx formatting](https://pythonhosted.org/an_example_pypi_project/sphinx.html)
* Take [MySQLRaidRespository](thesheriff/infrastructure/repository/mysql_raid_repository.py) as example
* If adding a new module, you'll need to add it to [index.rst](thesheriff/doc/source/index.rst) so it's added to the proper sections
* Generate new HTML contents
  ```console
  $ cd doc
  $ make html
  ```
  Open a web browser and point it to `file:///path/to/thesheriff/root/directory/doc/build/html/index.html`.