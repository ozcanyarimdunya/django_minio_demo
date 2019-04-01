import logging
from .base import *

logger = logging.getLogger()
logger.error("CURRENT MODE: /// %s ///" % os.getenv('MODE', 'DEVELOPMENT'))

if os.getenv('MODE') == 'PRODUCTION':
    from .production import *
else:
    from .local import *
