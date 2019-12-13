import logging.handlers

LOG_FILE = 'log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5,
                                               encoding='utf-8')  # 实例化handler
# fmt = '%(asctime)s - %(levelname)s - %(message)s'
fmt = '%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'

formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter

logger = logging.getLogger('test')  # 获取名为test的logger 默认是root
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)

logger.info(u'输出中文试一试')
logger.error("我写个中文看是不是乱码的。")
logger.debug('first debug message')
