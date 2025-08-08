import os
from datetime import datetime

from settings import LOGS_DIR


class Logger:
    def __init__(self, cam_ip):
        now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.log_file = os.path.join(LOGS_DIR, f"{cam_ip}_{now_str}.log")

        os.makedirs(LOGS_DIR, exist_ok=True)
        with open(self.log_file, 'a'):
            pass

    def write(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")
        print(message)