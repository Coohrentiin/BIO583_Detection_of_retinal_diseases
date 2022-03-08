from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy
from skimage.filters import threshold_otsu,sobel,sobel_v,sobel_h 
from scipy import ndimage
import os
from os import listdir
from os.path import isfile, join
from PIL import Image
from scipy import io
import pandas as pd
from scipy import ndimage
from scipy import signal
import skimage.filters as skifilt
import skimage.segmentation as skiseg
import skimage.morphology as skimorph
import cv2

def mask(input,sigma=9,area_threshold=2000):
	i_gauss = ndimage.gaussian_filter(input,sigma)
	i_gauss = (i_gauss-np.min(i_gauss))/(np.max(i_gauss)-np.min(i_gauss))
	i_sobel_v=scipy.ndimage.sobel(i_gauss, axis=0, output=None, mode='reflect', cval=0.0)
	i_sobel_h=scipy.ndimage.sobel(i_gauss, axis=1, output=None, mode='reflect', cval=0.0)

	i_sobel=i_sobel_v #+i_sobel_h**2
	i_normalized=i_sobel
	tho = skifilt.threshold_otsu(i_normalized)
	i_bw = i_normalized<tho
	i_rh = skimorph.remove_small_holes(i_bw,area_threshold)

	kernel = np.ones((20,20),np.uint8)
	i_rh_8 = np.array(1-i_rh, dtype=np.uint8)
	i_closing = cv2.morphologyEx(i_rh_8, op=cv2.MORPH_CLOSE,kernel=kernel)
	return(i_closing)

def first_layer(im):
    n,m = im.shape
    position=[]
    for i in range(m): #for each A scan
        ascan=im[:,i]
        max_pos = np.argmax(ascan)
        position.append(max_pos)
    return(position)

def first_layer_bottom(im,layer):
    n,m = im.shape
    position=[]
    for i in range(m):
        ascan=im[:,i]
        ascan=ascan[int(layer[i])+1:]
        max_pos = np.argmin(ascan)+int(layer[i])
        position.append(max_pos)
    return(position)

def last_layer(im):
    n,m = im.shape
    position=[]
    for i in range(m):
        ascan=im[:,i]
        ascan=ascan[::-1]
        max_pos = np.argmax(ascan)
        position.append(n-max_pos)
    return(position)

def last_layer_top(im,layer):
    n,m = im.shape
    position=[]
    for i in range(m):
        ascan=im[:,i]
        ascan=ascan[:int(layer[i])-1]
        ascan=ascan[::-1]
        max_pos = np.argmin(ascan)
        position.append(int(layer[i])-max_pos)
    return(position)

def jump_filter(layer,jump=10,offset=1):
    new_layer=layer
    for i in range(offset,len(layer)):
        if( np.abs(new_layer[i-offset]-new_layer[i])>jump ):
            if np.abs(new_layer[i]-new_layer[i-offset])<np.abs(new_layer[i]-layer[i-offset]):
                new_layer[i]=new_layer[i-offset]
            else:
                new_layer[i]=layer[i-offset]
    return(new_layer)

def golay_filter(layer):
    layer_smooth=signal.savgol_filter(layer,polyorder=2, window_length=51, deriv=0, delta=10.0, axis=- 1, mode='interp', cval=0.0)
    return(layer_smooth)


def layers(i_closing,jump=10,offset=1):
	f_l=first_layer(i_closing)
	# f_l=jump_filter(f_l,jump,offset)
	f_l=golay_filter(f_l)

	b_f_l=first_layer_bottom(i_closing,f_l)
	# b_f_l=jump_filter(b_f_l,jump,offset)
	b_f_l=golay_filter(b_f_l)

	l_l=last_layer(i_closing)
	# l_l=jump_filter(l_l,jump,offset)
	l_l=golay_filter(l_l)

	t_l_l=last_layer_top(i_closing,l_l)
	# t_l_l=jump_filter(t_l_l,jump,offset)
	t_l_l=golay_filter(t_l_l)
	return(f_l,l_l,b_f_l,t_l_l)
# np.where(layer==None)

def TR_layers(layers):
    f_l,l_l,b_f_l,t_l_l=layers
    return(l_l-f_l)

def RPEDC_layers(layers):
    f_l,l_l,b_f_l,t_l_l=layers
    return(l_l-t_l_l)

def NSR_layers(layers):
    f_l,l_l,b_f_l,t_l_l=layers
    return(t_l_l-f_l)

def Convexity_layers(layers,ascan_step,lateral_step):
    f_l,l_l,b_f_l,t_l_l=layers
    layer_smooth=signal.savgol_filter(l_l,polyorder=2, window_length=51, deriv=2, delta=10.0, axis=- 1, mode='interp', cval=0.0)
    val=np.sum(lateral_step*np.abs(layer_smooth))
    return(val)

def compute_folder(path,type_name,ascan_step,lateral_step,upper_limit,lower_limit,std_RPEDC,crop):
	files = [f for f in listdir(path) if isfile(join(path, f))]
	TR=[]
	RPEDC=[]
	NSR=[]

	df_QT=[]
	for f in files:
		try:
			image = mpimg.imread(os.path.join(path,f))
			if len(image.shape)>1:
				image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			image=image[:-crop,:]
			# i_closing=mask(image_normal)
			# layers_=layers(i_closing)
			i_closing=mask(image,sigma=5,area_threshold=2000)
			layers_=layers(i_closing,jump=20,offset=1)
			TR.append(TR_layers(layers_))
			RPEDC.append(RPEDC_layers(layers_))
			NSR.append(NSR_layers(layers_))
			parameters={
				'TR': TR_layers(layers_)*ascan_step,
				'RPEDC': RPEDC_layers(layers_)*ascan_step,
				'NSR': NSR_layers(layers_)*ascan_step,
				'Convexity': Convexity_layers(layers_,ascan_step,lateral_step),
				'Type': type_name,
				'Origin': f
			}
			df_QT.append(parameters)
		except:
			print("Error with "+f)
    # Compute AREA
	df_QT=pd.DataFrame(df_QT)
	df_QT["TR_A"]=df_QT["TR"].apply(np.sum)*ascan_step
	df_QT["RPEDC_A"]=df_QT["RPEDC"].apply(np.sum)*ascan_step
	df_QT["NSR_A"]=df_QT["NSR"].apply(np.sum)*ascan_step
	# Compute SCORE
	tho=200
	n=len(upper_limit)
	thickness_excess_=df_QT["RPEDC"].apply(lambda x: (x[:n]+x[len(x)-n:])/2-upper_limit)
	thickness_excess_=thickness_excess_.apply(lambda x: x*(x>0)*std_RPEDC)
	thickness_excess_=thickness_excess_.apply(np.sum)
	thickness_excess_[thickness_excess_>tho]=tho
	df_QT["thick_score"]=thickness_excess_

	thinness_excess_=df_QT["RPEDC"].apply(lambda x: lower_limit-(x[:n]+x[len(x)-n:])/2)
	thinness_excess_=thinness_excess_.apply(lambda x: x*(x>0)*std_RPEDC)
	thinness_excess_=thinness_excess_.apply(np.sum)
	thinness_excess_[thinness_excess_>tho]=tho
	df_QT["thin_score"]=0#thinness_excess_
	return([df_QT,TR,RPEDC,NSR])