from RMLibs.logging.RMLogger import RMLogger
from RMLibs.util.DateTimeUtil import DateTimeUtil
from farsight.config.Config import Config
from farsight.dao.Sample import Sample
from farsight.database.FSDbManager import FSDbManager

config_file: str = "./farsight/data/config.json"
config: Config = Config(config_file)

logger: RMLogger = RMLogger()
logger.file_name = "FarSight"
logger.log_path = config.log_path
logger.level = eval("RMLogger." + config.debug_level)
logger.verbose = eval(config.verbose)

db: FSDbManager = FSDbManager(config, logger)

