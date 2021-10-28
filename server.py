"""
Main module of the server file
"""
# local modules
import config
import os

# Get the application instance
connex_app = config.connex_app

# # Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")


def main(environ, start_response):
    port = int(os.environ.get('PORT', 5000))
    connex_app.run(host='0.0.0.0', port=port, debug=False)