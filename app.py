import connexion

from injector import Binder
from flask_injector import FlaskInjector
from connexion.resolver import RestyResolver

from services.provider import ItemsProvider

def configure(binder: Binder) -> Binder:
    binder.bind(
        ItemsProvider,
        ItemsProvider([{"Name": "Test 1"}])
    )


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='swagger/')
    app.add_api('my_super_app.yaml', resolver=RestyResolver('api'))
    # app.add_api('my_super_app.yaml')
    app.run(host='0.0.0.0', debug=True,threaded=True)
    # app.run()