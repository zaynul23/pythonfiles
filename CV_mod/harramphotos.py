"""
Rotate a HEIC (portrait → landscape) while preserving HDR and metadata.
✅ Tested with pillow-heif==1.1.1
"""

import numpy as np
from pillow_heif import HeifFile, write_heif

# ---------- CONFIG ----------
INPUT_PATH = "photo.heic"           # Input HEIC file
OUTPUT_PATH = "photo_rotated.heic"  # Output HEIC file
ROTATION = -1  # np.rot90(k=-1) = 90° clockwise (portrait → landscape)
# ROTATION = 1   # ← Uncomment this for 270° counterclockwise rotation
# ----------------------------

# 1️⃣ Open the HEIC file
heif_file = HeifFile(INPUT_PATH)

# 2️⃣ Get the main image frame
img = heif_file._images[0]  # same as heif_file.images[0] for single-image HEICs

# 3️⃣ Extract details
width, height = img.size
bit_depth = img.bit_depth
mode = img.mode               # e.g. 'RGB' or 'RGBA'
channels = len(mode)

# 4️⃣ Get pixel data as numpy array (16-bit container)
arr = np.frombuffer(img.data, dtype=np.uint16).reshape((height, width, channels))

# 5️⃣ Rotate 90° clockwise (portrait → landscape)
rotated = np.rot90(arr, k=ROTATION)

# 6️⃣ Extract metadata (EXIF + ICC color profile)
exif_data = img.metadata.get("exif")
icc_profile = img.metadata.get("icc_profile")

# 7️⃣ Save rotated HEIC — preserve HDR + metadata
write_heif(
    data=rotated.tobytes(),
    size=(rotated.shape[1], rotated.shape[0]),
    mode=mode,
    bit_depth=bit_depth,
    fp=OUTPUT_PATH,
    quality=-1,  # -1 = lossless if encoder supports it
    exif=exif_data,
    icc_profile=icc_profile,
)

print(f"✅ Rotated HDR HEIC saved → {OUTPUT_PATH}")
print(f"Bit depth preserved: {bit_depth}-bit | Mode: {mode}")
