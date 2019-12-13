import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    # filename="log.txt",
                    # filemode="w"
                    )

# logger = logging.getLogger(__name__)
# logger.error("abc%s{name}", '3')
# logging.error("44")
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'connection reset', extra=d)

# logging.info("abc%s", 'hello', extra=d)
# logger.warning("abc%s", 'hello', extra=d)
