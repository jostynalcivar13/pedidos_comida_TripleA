import logging
from pygelf import GelfUdpHandler
import json
from pythonjsonlogger import jsonlogger

def setup_graylog_logger(app_name="flask-app", graylog_host="graylog", graylog_port=12201):
    """Configurar logger para Graylog"""
    
    # Crear handler para Graylog
    graylog_handler = GelfUdpHandler(
        host=graylog_host,
        port=graylog_port,
        include_extra_fields=True,
        debug=True
    )
    
    # Configurar formato JSON para logs locales
    json_handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        '%(asctime)s %(name)s %(levelname)s %(message)s'
    )
    json_handler.setFormatter(formatter)
    
    # Configurar logger
    logger = logging.getLogger(app_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(graylog_handler)
    logger.addHandler(json_handler)
    
    return logger
