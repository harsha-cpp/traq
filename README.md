# TRAQ-Vision — Go API + YOLO Worker (Base Scaffold)

Base repository for a hackathon-style traffic video analytics system:
- **Go API**: job creation, status, artifact serving
- **Python worker**: YOLO imports + standard outputs (placeholders allowed)

## What this repo gives you
- Upload a video + config → create a job
- Run a local worker (Python) from Go
- Write predictable artifacts per job:
  - `runs/<job_id>/annotated.mp4`
  - `runs/<job_id>/metrics_queue.csv`
  - `runs/<job_id>/violations.json`
  - `runs/<job_id>/config_used.json`

---

## Tech Stack
- Go API: Go 1.25+
- Worker: Python 3.11+
- Vision libs: Ultralytics YOLO + OpenCV + NumPy + Pandas + PyTorch

---

## Repo Structure