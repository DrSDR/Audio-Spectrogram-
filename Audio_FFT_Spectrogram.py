

# made by thegmr140  on youtube
# program reads in jpeg image and converts to audio spectrogram.
# user can select image file and save as audio wave file
#  best to have simple text photos









import numpy as np  # N-dimensional arrays
# from scipy.signal import firwin, lfilter  # filtering

from PIL import Image  # read images 

# from skimage.io import imread  # read an image file
from scipy.io import wavfile  # writing wav files

import matplotlib.pyplot as plt  # showing an image plot

from tkinter import filedialog  # open/save a file through GUI

h = 800
w = 400
imsize = (h,w)

# import sys  # aborting the script

filename = filedialog.askopenfilename()  # get a jpg file, window pops up, go get jpg
data = Image.open(filename)   # open the jpg file
data = data.resize( (w,h) )


data = np.array(data,dtype='float')      # turn jpg into [w x h x 3]  matrix of numbers


# convert the jpg to grayscale using 1950s NTCS math
# now we lazy and just code it.
data = 0.2989*data[:,:,0] + 0.5870*data[:,:,1] + 0.1140*data[:,:,2]   # grayscale math old school
# data is now a [w x h]  matrix,     so 3d to 2d

data = data / np.max(data)
data = np.flip(data,axis=0)

phdata = np.random.randn(h,w)
phdata = 23 * phdata
phdata = np.exp(1j * phdata)

data = data * phdata
d2 = data
d1 = np.flip(data,axis=1)
d1 = d1[: , 0:-1]
d1 = np.conjugate(d1)

data = np.concatenate( (d1,data) , axis=1)

data = np.fft.ifftshift(data,axes=1)
data = np.fft.ifft(data,axis=1)




#flatten matrix into 1xN vector
data = data.flatten();    # 1xN vector
data = np.real(data)

# normalize to -1 to 1 range
data = data / np.max(data)

#now scale to int16 range  -32768 to 32767
data = np.multiply(data,32767)



# 2ch wave file
data = np.array([np.real(data), np.real(data)]).T  # need transpose since wavefile.write expects shape (Nsamples, Nchannels)
data = data.astype(np.int16)  # int16


# # see the signal before wav file save
# plt.figure(4)
# plt.plot(data[:,0],label='real data')
# plt.plot(data[:,1],label='imag data')
# plt.legend()
# plt.title('I/Q time signal int16 ranges')
# plt.show()


filetypes = [('WAV File', '*.wav')]
pathname = filedialog.asksaveasfilename(filetypes=filetypes, defaultextension=filetypes)

fs = 24e3  # sampling freq of wave file


wavfile.write(pathname, int(round(fs)), data )  # sampling rate needs to be an integer (samples per sec)










