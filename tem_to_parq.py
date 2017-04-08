# Imports
from skimage import io

import pandas as pd

import fastparquet as fp

import numpy as np

import os

# Read file from the disk
filename = 'TiltSeries_NanoParticle_doi_10.1021-nl103400a.tif'
filenamePrefix = os.path.splitext(os.path.basename(filename))[0]

im = io.imread(filename)

# Reshape 3D to one giant 2D
imgdata2d = im.reshape(im.shape[0] * im.shape[1], im.shape[2])
index = range(0, im.shape[0] * im.shape[1])

# Convert to Pandas dataframe
df = pd.DataFrame(imgdata2d.astype(np.int32),
                  columns=[str(i) for i in range(0, 256)],
                  index=index)

# Write it out as Parquet format
fp.write(''.join([filenamePrefix, '.parq']), df, compression='GZIP')
