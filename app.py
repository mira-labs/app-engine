# app.py

from flask import Flask
from flask_graphql import GraphQLView
from graphql import GraphQLSchema, build_ast_schema, parse
from graphql.queries import Query  # Import the Query class from graphql folder
import os

app = Flask(__name__)

# Load the GraphQL schema from the file
schema_path = os.path.join(os.path.dirname(__file__), "schema.graphql")
with open(schema_path, "r") as file:
    schema_definition = file.read()

schema = build_ast_schema(parse(schema_definition))

# Add the GraphQL view to the app
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    methods=["GET", "POST"],
)

if __name__ == "__main__":
    app.run(debug=True)
