The Sheriff Usage
=================

Runtime Requirements
--------------------

To run and validate the application locally, the following tools are required:

- `Docker Compose <https://docs.docker.com/compose/>`_
- `Curl <https://curl.haxx.se/>`_
- `GNU Make <https://www.gnu.org/software/make/>`_

The project includes a *Makefile* with the following targets:

- **run**: cleans previously built images and runs the stack,
  the application and the DB.
- **lint**: runs *pycodestyle* over the *thesheriff* and tests directories,
  and reports any linting problems on the code.
- **tests**: runs *pytest* and reports the results
  of the unit tests.

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
      {"message": "Outlaw created successfully", "outlaw": {"id": "1", "name": "Outlaw", "email": "outlaw@yopmail.com"}}

- Create a Gang

  .. code-block:: console

     $ curl localhost:5000/api/v1/gang/ -X POST \
       --data @examples/json/create_gang.json \
       -H 'Content-Type: application/json'
     {"message": "Gang created successfully", "gang": {"name": "The best gang", "members": [], "created_raids": 0, "owner_id": 1, "id": 1}}

- Create a Raid

  .. code-block:: console

    $ curl http://localhost:5000/api/v1/raid -X POST \
      -H 'Content-Type: application/json' \
      --data @examples/json/create_raid.json
      {"message":"Raid created successfully","raid":{"id":1,"name":"Asalto 1"}}

- List all Gangs

  .. code-block:: console

     $ curl localhost:5000/api/v1/gang
     {"message":"Sucess", "gangs":[{"id":1,"name":"The best gang"},{"id":2,"name":"The best gang"}]}

Tests
-----

This section is strongly related to the previous one. To validate the use cases, there have been
developed a set of unit tests. These tests can be found in *tests* folder, in the root.

The available tests are:

- Create gang test

- Create outlaw test

- Create raid test

- End raid test

- List gangs test (from gang)

- Grade raid test

- Invite friends test

- Join gang test

- List friends test

- List gangs test (from outlaw)

- Rate raid test

These tests use the next mocked objects (depending on the use case):

- Mock gang repository

- Mock mail notifier

- Mock outlaw repository

- Mock raid repository

In general, these unit tests trigger a specific use case, injecting to it a mock repository or notifier,
and passing it specific information through a request object.
These mock repositories are necessary to hard-code information that should be received through
these interfaces. This information is needed to fulfill the intended functionality or to conclude that
the software is working properly.
Finally, depending of which value is returned after executing the use case, the test pass or not.

Development Requirements
------------------------

To hack on the application, the following tools are required:

- `Python >= 3.8 <https://www.python.org>`_
- `pipenv <https://pipenv.readthedocs.io/en/latest/>`_
- `GNU make <https://www.gnu.org/software/make/>`_
- `Git <https://git-scm.com/>`_
