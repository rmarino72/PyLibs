import threading

from RMLibs.logging.RMLogger import RMLogger
from farsight.bl.DataProducer import DataProducer
from farsight.config.Config import Config
from farsight.database.FSDbManager import FSDbManager


config_file: str = "./farsight/data/config.json"
config: Config = Config(config_file)

logger: RMLogger = RMLogger()
logger.file_name = "FarSight"
logger.log_path = config.log_path
logger.level = eval("RMLogger." + config.debug_level)
logger.verbose = eval(config.verbose)

db: FSDbManager = FSDbManager(config, logger)

producer: DataProducer = DataProducer()
producer.logger = logger
producer.config = config
producer.db = db


producer.run()