import logging

delivery_date_logger = logging.getLogger('delivery_date_logger')
delivery_date_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('calculations.log')

delivery_date_logger.addHandler(file_handler)