## Camera Recording Automation

This project provides a Python-based solution to automate continuous recording from multiple IP cameras using FFmpeg. It supports segmented recordings, automatic retries on failure, and per-camera logging.
Features

- Records multiple RTSP cameras in parallel using separate processes
- Segments video files by configurable time intervals (e.g., hourly files)
- Automatic retry mechanism on FFmpeg failure with configurable max attempts
- Detailed logging per camera with timestamped log files
- Desktop notifications on recording interruptions or completion (Linux notify-send)
- Easy configuration via .env and a camera address list file

#### Requirements

- Python 3.7+
- FFmpeg installed and available in your system PATH
- python-dotenv package (pip install python-dotenv)
- Linux environment with notify-send available (for desktop notifications)

### Setup
1. Clone this repository
2. Create a .env file with your configuration variables:
    ```env
    LOGS_DIR=/path/to/logs
    RECORDS_DIR=/path/to/recordings
    RTSP_USER=your_camera_username
    RTSP_PASSWORD=your_camera_password
    RTSP_IP=your_camera_ip
    RTSP_PORT=554
    SEGMENT_TIME=3600
    MAX_ATTEMPTS=3
    ```
3. Create a file camera-address-list.txt listing each camera's RTSP URL or IP (one per line).

4. Install dependencies:
```
pip install python-dotenv
```

### Usage

Run the main script to start recording all cameras in parallel:

python main.py

Each camera will record segmented videos and logs will be saved under the specified directories.
### Logging

Logs are generated per camera with timestamps to help debug any issues during recording.
### Troubleshooting

- Make sure FFmpeg is properly installed and accessible from your command line
- Check file permissions on log and recordings directories
- Confirm camera credentials and network accessibility