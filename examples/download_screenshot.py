"""VTGraph get screenshot."""

import khulnasoft_graph_api

API_KEY = ""  # Insert your VT API here.
GRAPH_ID = ""  # Insert yout graph id here.

# Retrieve the graph.
graph = khulnasoft_graph_api.VTGraph.load_graph(GRAPH_ID, API_KEY)

# Download screenshot
graph.download_screenshot(path=".")
