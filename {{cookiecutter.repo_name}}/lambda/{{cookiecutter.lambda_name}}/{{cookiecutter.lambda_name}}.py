import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)


# This is the method that will be registered
# with Lambda and run on a schedule
def handler(event={}, context={}):
  if 'ping' in event:
    logger.info('pong')
    return {'message': 'pong'}

  logger.info('hello world')
  return {'message': 'Hello World'}

# If being called locally, just call handler
if __name__ == '__main__':
  logging.basicConfig()
  handler()
