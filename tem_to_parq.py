from skimage import io
import pandas as pd
import fastparquet as fp

im = io.imread('TiltSeries_NanoParticle_doi_10.1021-nl103400a.tif')
imgdata2d = im.reshape(im.shape[0] * im.shape[1], im.shape[2])
index = range(0, im.shape[0] * im.shape[1])

df = pd.DataFrame(imgdata2d, columns=[str(i) for i in range(0, 256)], index=index)
fp.write('out.parq', df, compression='GZIP')


