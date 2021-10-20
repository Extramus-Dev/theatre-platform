import pymysql
import dotenv
import logging

# configure the log with DEBUG level
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S')

dotenv.load_dotenv()
pymysql.install_as_MySQLdb()

logger = logging.getLogger('Server_api_django')