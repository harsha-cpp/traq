from ultralytics import YOLO
import cv2
import numpy as np
import pandas as pd
import json
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--job_id", required=True)
    parser.add_argument("--video", required=True)
    parser.add_argument("--config", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    pass


if __name__ == "__main__":
    main()
