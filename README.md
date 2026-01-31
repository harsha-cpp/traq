# TRAQ-Vision

AI-powered traffic video analytics system for **queue analysis** and **rule violation detection** from **pre-recorded CCTV footage**.

## What it does
- Detects common vehicle types (car, bike/scooter, auto, bus, truck)
- Tracks vehicles over time (consistent IDs)
- Estimates:
  - **Queue length** (how many vehicles are waiting)
  - **Queue density / occupancy** (how crowded the waiting area is)
- Flags:
  - **Red-light jumping** (crossing the stop line during red)
  - **Rash driving (risk flags)** using explainable motion/trajectory rules
- Produces:
  - **Annotated video**
  - **Metrics reports**
  - **Violation event list with evidence**

## Outputs
Each run generates:
- Annotated video (with boxes, IDs, and event markers)
- Queue metrics over time (length + density/occupancy)
- Violation log (event time, vehicle type, reason, evidence frames)

## How it works (high level)
1. Video is processed frame-by-frame
2. Vehicles are detected and assigned track IDs
3. Queue metrics are computed inside defined queue zones near the stop line
4. Violations are detected using stop-line crossing + motion heuristics
5. Results are shown in a web dashboard (Next.js) and exported as files

## Why this matters
- Reduces manual monitoring effort
- Enables data-driven congestion insights
- Provides evidence-backed review for violations
- Supports safer, smarter intersection management

## Folder Structure

```
.
├── api/                        # Go REST API
│   ├── cmd/server/             # Main entrypoint
│   └── internal/
│       ├── handlers/           # HTTP handlers
│       ├── jobs/               # Job model & management
│       └── storage/            # Filesystem storage
├── worker/                     # Python YOLO worker
│   └── worker/run.py           # Worker entrypoint
├── configs/                    # Job configuration files
├── inputs/                     # Input videos
└── runs/                       # Output artifacts per job
    └── {job_id}/
        ├── annotated.mp4
        ├── metrics_queue.csv
        ├── violations.json
        └── config_used.json
```

## Notes
This project is designed for **hackathon/demo use** and focuses on **explainable analytics**, not full production deployment.
