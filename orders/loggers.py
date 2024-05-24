import logging

vms_logger = logging.getLogger('delivery_date_logger')

vms_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('calculations.log')

vms_logger.addHandler(file_handler)