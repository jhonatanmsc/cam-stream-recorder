import os
import subprocess
import time
from multiprocessing import Process

from log_entry import Logger
from settings import segment_time, RECORDS_DIR, max_attempts
from utils import export_ip_only


def record_camera(cam_ip):
    ip_only = export_ip_only(cam_ip)
    ffmpeg_command = [
        'ffmpeg',
        '-i', cam_ip,
        '-c:v', 'copy',
        '-c:a', 'pcm_alaw',
        '-f', 'segment',
        '-segment_time', str(segment_time),
        '-strftime', '1',
        os.path.join(RECORDS_DIR, f'{ip_only}_%Y-%m-%d_%H-%M-%S.mkv')
    ]

    log = Logger(ip_only)
    log.write("command: " + ' '.join(ffmpeg_command))

    attempt_counter = 0
    while attempt_counter < max_attempts:
        try:
            result = subprocess.run(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            log.write(result.stdout)

            if result.returncode != 0:
                attempt_counter += 1
                log.write(f"FFmpeg failed. Attempt {attempt_counter} of {max_attempts}.")
                if attempt_counter == max_attempts:
                    log.write("Maximum number of attempts reached. Exiting...")
                    subprocess.run(["notify-send", "The recording was interrupted"])
                    break
                time.sleep(5)
            else:
                log.write("FFmpeg executed successfully.")
                break

        except Exception as e:
            attempt_counter += 1
            log.write(f"Unexpected error: {e}. Attempt {attempt_counter} of {max_attempts}.")
            if attempt_counter == max_attempts:
                log.write("Maximum number of attempts reached due to an error. Exiting...")
                subprocess.run(["notify-send", "The recording was interrupted"])
                break
            time.sleep(5)

def main():
    cam_ip_list = []
    with open('camera-address-list.txt', 'r') as file:
        cam_ip_list = [ip.strip() for ip in file.readlines()]

    processes = []
    for cam_ip in cam_ip_list:
        p = Process(target=record_camera, args=(cam_ip,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    subprocess.run(["notify-send", "The recording has ended"])

if __name__ == '__main__':
    main()
