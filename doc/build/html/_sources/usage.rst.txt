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
- **docs**

Validating use cases
--------------------

To run a complete validation of all the working use cases, a *validate.sh*
script has been included in the root of the project, it creates
the required objects and show the results, to run the automated validation
please do as follows:

.. code-block:: console

  $ bash validate.sh

The output informs at any point of the actions being taken and prints
the results.

For manually running the validation, here are the steps to take:

- Start the stack

  .. code-block:: console

    $ make run

- Create an Outlaw

  .. code-block:: console

    $ curl localhost:5000/api/v1/outlaw -X POST \
      --data @examples/json/create_outlaw_1.json \
      -H 'Content-Type: application/json'

     {"message":"Outlaw created successfully","outlaw":{"email":"reallybad@yopmail.com","id":1,"name":"The bad one"}}

- Create a Gang

  .. code-block:: console

    $ curl localhost:5000/api/v1/gang -X POST \
      --data @examples/json/create_gang.json \
      -H 'Content-Type: application/json'

     {"gang":{"id":1,"name":"The best gang","owner_id":"1"},"message":"Gang successfully created"}

- Create a Raid

  .. code-block:: console

    $ curl http://localhost:5000/api/v1/raid -X POST \
      -H 'Content-Type: application/json' \
      --data @examples/json/create_raid.json

     {"message":"Raid created successfully","raid":{"id":1,"name":"Raid 1"}}

- Rate a Raid

  .. code-block:: console

    $ curl localhost:5000/api/v1/raid/1/rate -X PUT \
      --data @examples/json/rate_raid.json \
      -H 'Content-Type: application/json'

     {"message":"Raid rated successfully"}

- End a Raid

  .. code-block:: console

    $ curl localhost:5000/api/v1/raid/1/end \
      -X PUT -H 'Content-Type: application/json'

     {"message":"raid finished successfully","score":"Gang's score: 0.0. Sheriff's score on raid 'Raid 1': 6.625"}

- List all Gangs

  .. code-block:: console

    $ curl localhost:5000/api/v1/gang

     {"gangs":[{"id":1,"name":"The best gang"}],"message":"Success"}

- List Outlaw Gangs

  .. code-block:: console

    $ curl localhost:5000/api/v1/outlaw/1/gangs

     {"gangs":[],"message":"Success"}

- Invite a Friend

  .. code-block:: console

   $ curl localhost:5000/api/v1/outlaw/1/invite_friend \
     -X POST --data @examples/json/invite_friend.json \
     -H 'Content-Type: application/json'

    {"message":"Invitation sent successfully"}

Tests
-----

This section is strongly related to the previous one. To validate
the use cases, there have been developed a set of unit tests.
These tests can be found in *tests* folder, in the root.

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

In general, these unit tests trigger a specific use case, injecting
to it a mock repository or notifier, and passing it specific
information through a request object.
These mock repositories are necessary to hard-code information that
should be received through these interfaces. This information is needed
to fulfill the intended functionality or to conclude that the software
is working properly. Finally, depending of which value is returned
after executing the use case, the test pass or not.

Development Requirements
------------------------

To hack on the application, besides the tools on listed on runtime section
above, the following ones are required:

- `Python >= 3.8 <https://www.python.org>`_
- `pipenv <https://pipenv.readthedocs.io/en/latest/>`_
- `Git <https://git-scm.com/>`_
