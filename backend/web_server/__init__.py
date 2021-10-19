import pymysql
import dotenv
import logging
import os

# configure the log with DEBUG level
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S')

pymysql.install_as_MySQLdb()
dotenv.load_dotenv()

logger = logging.getLogger('ServerApi')
logger.info("Environ Variable DB_HOST: " + os.environ.get('DB_HOST', default='null'))
logger.info("Environ Variable DB_PORT: " + os.environ.get('DB_PORT', default='null'))