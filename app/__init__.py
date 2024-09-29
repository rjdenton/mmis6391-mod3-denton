from .app_factory import create_app
from .db import get_db_connection
from .app_factory import create_app

app = create_app()

from . import routes
