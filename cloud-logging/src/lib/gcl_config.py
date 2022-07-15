""" Google Cloud logging import """
from google.cloud import logging
from google.cloud.logging import DESCENDING
import google.cloud.logging

""" 1-way to initialized google cloud logging"""
# GOOGLE_APPLICATION_CREDENTIALS=keys/kai-testing-342914-4c856bb8c132.json
# GOOGLE_APPLICATION_CREDENTIALS = keys/gcp-logging-avyay-47e31da82aeb.json
# GOOGLE_APPLICATION_CREDENTIALS=/keys/kai-product-classification-04b8c49a5a6a.json
# service_key_path = "keys/gcp-logging-avyay-47e31da82aeb.json"
# logging_client = logging.Client.from_service_account_json(service_key_path)
# logger = logging_client.logger(log_name_kai)

""" 2-way to initialized google cloud logging"""
# logging_client.setup_logging()
# logging_client = logging.Client()
# logger = logging_client.logger(log_name_kai) 

service_key_path  = "keys/lofty-totality-351508-c4d87ea2af59.json"
def gcl_client(logger_name):
    logging_client = logging.Client.from_service_account_json(service_key_path)
    logger = logging_client.logger(logger_name)
    # client = logging.Client()
    # logger = client.logger(logger_name)
    return logging_client, logger