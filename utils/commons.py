import io

import cv2
import numpy as np


def read_image_from_Bytes(file):
    return cv2.imdecode(np.frombuffer(io.BytesIO(file).read(), np.uint8), 1)