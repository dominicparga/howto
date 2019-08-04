#!/usr/bin/env python

'''
This file shows examples playing with images in python.
A big help was
https://matplotlib.org/3.1.0/tutorials/introductory/images.html#sphx-glr-tutorials-introductory-images-py
'''
__author__ = 'Dominic Parga Cacheiro'
__credits__ = 'Dominic Parga Cacheiro,'

import os
import matplotlib.pyplot as plt
import numpy as np

#-----------------------------------------------------------------------------#
# constants

ROOT = os.path.join(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
RESOURCES = os.path.join(ROOT, 'resources')
CONSTANTS = {
    'paths': {
        'root': ROOT,
        'res': RESOURCES,
        'imgs': {
            'orig': os.path.join(RESOURCES, 'original_512x512.png'),
        }
    },
}

#-----------------------------------------------------------------------------#
# image functions

def width(img):
    return img.shape[0]

def height(img):
    return img.shape[1]

def scale_channels(img, c0=1, c1=1, c2=1, c3=1):
    img[:, :, 0] *= c0
    img[:, :, 1] *= c1
    img[:, :, 2] *= c2
    img[:, :, 3] *= c3
    return img

def rm_alpha(img):
    '''
    Return the values (width, height, 3) of the image (width, height, 4)
    without the alpha-column.
    '''
    return img[:, :, 0:3]

def reduce_channels(img, c_idx):
    for x in range(width(img)):
        for y in range(height(img)):
            c = img[x, y, c_idx]
            img[x, y, 0] = c
            img[x, y, 1] = c
            img[x, y, 2] = c
    return img

def rgba_to_YCbCra(
    img,
    weights=[
        [0.299, 0.587, 0.114],
        [-0.168736, -0.331264, 0.5],
        [0.5, -0.418688, -0.081312],
    ],
):
    '''
    Converts this rgba-image to a grayscale-image by calculating
    the brightness using the given 3 weights (rgb).

    Weights are normalized per default.

    Could be used to filter out channels, e.g. by
    weights=[1.0, 0.0, 0.0]
    '''

    # normalize and prepare for calculation
    weights = np.array(weights)

    # apply weights
    proto_img = np.apply_along_axis(
        lambda rgb: np.dot(rgb, weights),
            axis=2,
            arr=rm_alpha(img.copy())
    )
    proto_img[:, :, 1:3] += 0.5

    # update img
    for x in range(width(img)):
        for y in range(height(img)):
            for c_idx in range(3):
                c = proto_img[x, y, c_idx]
                # slight rounding-errors in proto_img (e.g. 1.0007247)
                img[x, y, c_idx] = max(0, min(c, 1))

    return img

def YCbCra_to_rgba(
    img,
    weights=[
        [0.299, 0.587, 0.114],
        [-0.168736, -0.331264, 0.5],
        [0.5, -0.418688, -0.081312],
    ],
):
    '''
    Converts this rgba-image to a grayscale-image by calculating
    the brightness using the given 3 weights (rgb).

    Weights are normalized per default.

    Could be used to filter out channels, e.g. by
    weights=[1.0, 0.0, 0.0]
    '''

    # normalize and prepare for calculation
    weights = np.linalg.inv(np.array(weights))

    img[:, :, 1:3] -= 0.5
    # apply weights
    proto_img = np.apply_along_axis(
        lambda ycc: np.dot(ycc, weights),
            axis=2,
            arr=rm_alpha(img.copy())
    )

    # update img
    for x in range(width(img)):
        for y in range(height(img)):
            for c_idx in range(3):
                c = proto_img[x, y, c_idx]
                # slight rounding-errors in proto_img (e.g. 1.0007247)
                img[x, y, c_idx] = max(0, min(c, 1))

    return img

#-----------------------------------------------------------------------------#
# application

def plot_rgba(img):
    fig = plt.figure('rgb')

    a = fig.add_subplot(2, 2, 1)
    imgplot = plt.imshow(img)
    a.set_title('original')

    a = fig.add_subplot(2, 2, 2)
    imgplot = plt.imshow(reduce_channels(img.copy(), 0))
    a.set_title('red')

    a = fig.add_subplot(2, 2, 3)
    imgplot = plt.imshow(reduce_channels(img.copy(), 1))
    a.set_title('green')

    a = fig.add_subplot(2, 2, 4)
    imgplot = plt.imshow(reduce_channels(img.copy(), 2))
    a.set_title('blue')

    plt.tight_layout()
    plt.show()

def plot_YCbCr(img):
    fig = plt.figure('YCbCr')

    a = fig.add_subplot(2, 2, 1)
    imgplot = plt.imshow(img)
    a.set_title('original')

    img = rgba_to_YCbCra(img)

    a = fig.add_subplot(2, 2, 2)
    imgplot = plt.imshow(reduce_channels(img.copy(), 0))
    a.set_title('luminance Y')

    a = fig.add_subplot(2, 2, 3)
    imgplot = plt.imshow(reduce_channels(img.copy(), 1))
    a.set_title('Cb')

    a = fig.add_subplot(2, 2, 4)
    imgplot = plt.imshow(reduce_channels(img.copy(), 2))
    a.set_title('Cr')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    '''
    Show examples of working with images.
    '''

    img = plt.imread(CONSTANTS['paths']['imgs']['orig'])
    print(img.shape)

    plot_rgba(img)
    plot_YCbCr(img)
