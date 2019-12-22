The Sheriff Usage
=================

The project includes a *Makefile* with the following targets:

- **run**: cleans previously built images and runs the stack,
  the application and the DB.
- **lint**: runs *pycodestyle* over the *thesheriff* directory
  and reports any linting problems on the code.
- **tests**: runs *pytest* and reports the results
  of the unit tests.

Runtime Requirements
--------------------

To run and validate the application locally, the following tools are required:

- `Docker Compose <https://docs.docker.com/compose/>`_
- `Curl <https://curl.haxx.se/>`_

Validating use cases
--------------------

- Start the stack

  .. code-block:: console

    $ make run

- Create an Outlaw

  .. code-block:: console

     $ curl localhost:5000/api/v1/outlaw/ -X POST \
       --data @examples/json/create_outlaw.json \
       -H 'Content-Type: application/json'
     {"message":"Outlaw added successfully","status":201}

Development Requirements
------------------------

To hack on the application, the following tools are required:

- `Python >= 3.8 <https://www.python.org>`_
- `pipenv <https://pipenv.readthedocs.io/en/latest/>`_
- `GNU make <https://www.gnu.org/software/make/>`_
- `Git <https://git-scm.com/>`_
