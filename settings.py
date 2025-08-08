# Carrega variáveis do arquivo .env
import os

from dotenv import load_dotenv

load_dotenv()

LOGS_DIR = os.getenv('LOGS_DIR')
RECORDS_DIR = os.getenv('RECORDS_DIR')
RTSP_USER = os.getenv('RTSP_USER')
RTSP_PASSWORD = os.getenv('RTSP_PASSWORD')
RTSP_IP = os.getenv('RTSP_IP')
RTSP_PORT = os.getenv('RTSP_PORT')

segment_time = os.getenv('SEGMENT_TIME', 3600)
max_attempts = os.getenv('MAX_ATTEMPTS', 3)