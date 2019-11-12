import redis
from redisgraph import Node, Edge, Graph
from flask import Flask, json
from logging.config import dictConfig


def create_app():
    """ Create and return the application object """
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
    app = Flask(__name__, instance_relative_config=True)
    #app.config.from_pyfile('config.py')

    @app.route("/", methods=["GET"])
    def index():
        r = redis.Redis(host="localhost", port=6379)
        redis_graph = Graph("TheSheriff", r)
        query = """MATCH (b:bandido)-[m:member {status:'sheriff'}]->(bb:banda) RETURN b.name, b.age, bb.name"""
        result = redis_graph.query(query)
        return json.jsonify(result.result_set)
    
    @app.route("/save", methods=["GET"])
    def save_value():
        r = redis.Redis(host="localhost", port=6379)
        redis_graph = Graph("TheSheriff", r)
        john = Node(label="bandido", properties={"name": "John Doe", "age": 33, "gender": "male", "status": "single"})
        jane = Node(label="bandido", properties={"name": "Jane Roe", "age": 30, "gender": "female", "status": "single"})
        banda00 = Node(label="banda", properties={"name": "banda00"})
        banda01 = Node(label="banda", properties={"name": "banda01"})
        banda02 = Node(label="banda", properties={"name": "banda02"})
        edge00 = Edge(john, "member", banda00, properties={"status": "sheriff"})
        edge01 = Edge(jane, "member", banda01, properties={"status": "sheriff"})
        edge02 = Edge(jane, "member", banda02, properties={"status": "sheriff"})
        edge03 = Edge(john, "member", banda02, properties={"status": "member"})
        redis_graph.add_node(john)
        redis_graph.add_node(jane)
        redis_graph.add_node(banda00)
        redis_graph.add_node(banda01)
        redis_graph.add_node(banda02)
        redis_graph.add_edge(edge00)
        redis_graph.add_edge(edge01)
        redis_graph.add_edge(edge02)
        redis_graph.add_edge(edge03)
        redis_graph.commit()
        return json.jsonify(result="success")

    return app