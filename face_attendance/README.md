# Face & Eyes Detection Attendance App (OpenCV)

Basic webcam attendance app using OpenCV Haar cascades for face and eye detection.

Usage

1. (Optional) Activate your Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python attendance.py
```

4. The webcam window shows detections. Press `q` to quit. Attendance is saved to `attendance.csv` in the same folder.

Notes

- This is a minimal example using Haar cascades included with OpenCV. It's not a production-grade face recognition system.
- The script assigns incremental labels like `Person_1`, `Person_2` as new faces are detected during the session.
