# The Sheriff

## Desarrollo

### Herramientas

* docker (docker-compose)

### Librerias

* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

### Aplicación

El directorio [thesheriff](thesheriff) será la raíz de la aplicación, el fichero [__init__.py](thesheriff/__init__.py) contiene la inicialización de la aplicación Flask, con el método *create_app()*.

### Ejecución

```console
$ docker-compose up
```

* Arranca los servicios *app* y *db*
* El nombre de host *db* se puede usar desde *app*
* *app* se publicará en el puerto *5000* en *localhost*