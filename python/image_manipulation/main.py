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
    'tasks': [
        'all', 'rgba-colored', 'rgba-grayscale', 'YCbCr', 'cmaps',
        'histogram', 'climmed'
    ],
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

def rm_channels(img, c0=False, c1=False, c2=False, c3=False):
    rm_idx = []
    if c0: rm_idx.append(0)
    if c1: rm_idx.append(1)
    if c2: rm_idx.append(2)
    if c3: rm_idx.append(3)
    img = np.delete(img, rm_idx, axis=2)
    if img.shape[-1] == 1:
        img = img.reshape(img.shape[0:-1])
    return img

def rm_alpha(img):
    '''
    Return the values (width, height, 3) of the image (width, height, 4)
    without the alpha-column.
    '''
    img = img[:, :, 0:3]
    return img

def equalize_channels(img, c_idx):
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

def plot_rgba_colored(img):
    title='rgb-colored'

    fig = plt.figure(title)

    a = fig.add_subplot(2, 2, 1)
    imgplot = plt.imshow(img)
    a.set_title('original')

    a = fig.add_subplot(2, 2, 2)
    imgplot = plt.imshow(scale_channels(img.copy(), 1, 0, 0))
    a.set_title('red')

    a = fig.add_subplot(2, 2, 3)
    imgplot = plt.imshow(scale_channels(img.copy(), 0, 1, 0))
    a.set_title('green')

    a = fig.add_subplot(2, 2, 4)
    imgplot = plt.imshow(scale_channels(img.copy(), 0, 0, 1))
    a.set_title('blue')

    print(title)
    plt.tight_layout()
    plt.show()

def plot_rgba_grayscale(img):
    title='rgb-grayscale'

    fig = plt.figure(title)

    a = fig.add_subplot(2, 2, 1)
    imgplot = plt.imshow(img)
    a.set_title('original')

    # by equalizing all color-channels
    a = fig.add_subplot(2, 2, 2)
    imgplot = plt.imshow(equalize_channels(img.copy(), 0))
    a.set_title('red')

    # or by removing all dimensions except for one
    a = fig.add_subplot(2, 2, 3)
    imgplot = plt.imshow(rm_channels(img.copy(), True, False, True, True))
    imgplot.set_cmap('gray')
    a.set_title('green')

    a = fig.add_subplot(2, 2, 4)
    imgplot = plt.imshow(rm_channels(img.copy(), True, True, False, True))
    imgplot.set_cmap('gray')
    a.set_title('blue')

    print(title)
    plt.tight_layout()
    plt.show()

def plot_YCbCr(img):
    title='YCbCr'

    fig = plt.figure(title)

    lum_img = img.copy()

    a = fig.add_subplot(2, 2, 1)
    imgplot = plt.imshow(lum_img)
    a.set_title('original')

    lum_img = rgba_to_YCbCra(lum_img)

    a = fig.add_subplot(2, 2, 2)
    imgplot = plt.imshow(equalize_channels(lum_img.copy(), 0))
    a.set_title('luminance Y')

    a = fig.add_subplot(2, 2, 3)
    imgplot = plt.imshow(equalize_channels(lum_img.copy(), 1))
    a.set_title('Cb')

    a = fig.add_subplot(2, 2, 4)
    imgplot = plt.imshow(equalize_channels(lum_img.copy(), 2))
    a.set_title('Cr')

    print(title)
    plt.tight_layout()
    plt.show()

def plot_cmaps(img):
    title='colormaps'

    fig = plt.figure(title)

    lum_img = rm_channels(rgba_to_YCbCra(
        img.copy()), c1=True, c2=True, c3=True
    )

    a = fig.add_subplot(2, 2, 1)
    imgplot = plt.imshow(lum_img, cmap='gray')
    a.set_title('cmap=\'gray\'')

    a = fig.add_subplot(2, 2, 2)
    imgplot = plt.imshow(lum_img, cmap='hot')
    a.set_title('cmap=\'hot\'')

    a = fig.add_subplot(2, 2, 3)
    imgplot = plt.imshow(lum_img, cmap='viridis')
    a.set_title('cmap=\'viridis\'')

    a = fig.add_subplot(2, 2, 4)
    imgplot = plt.imshow(lum_img, cmap='nipy_spectral_r')
    a.set_title('cmap=\'nipy_spectral_r\'')

    print(title)
    plt.tight_layout()
    plt.show()

def plot_hist(img):
    title='histograms-grayscale'

    fig = plt.figure(title)

    lum_img = rm_channels(rgba_to_YCbCra(
        img.copy()), c1=True, c2=True, c3=True
    )

    lum_img = 256 * lum_img

    a = fig.add_subplot(1, 2, 1)
    plt.hist(lum_img.ravel(), bins=256, range=(0, 255), fc='k', ec='k')
    a.set_title('0-255')

    a = fig.add_subplot(1, 2, 2)
    plt.hist(lum_img.ravel(), bins=256, range=(0, 254), fc='k', ec='k')
    a.set_title('0-254')

    print(title)
    plt.tight_layout()
    plt.show()

def plot_climmed(img):
    print('\'climmed\' is unsupported yet.')
    return

    # TODO
    title='climmed'

    fig = plt.figure(title)

    a = fig.add_subplot(1, 2, 1)
    imgplot = plt.imshow(lum_img, cmap='gray')
    a.set_title('Before')
    plt.colorbar(ticks=[25, 75, 125, 175], orientation='horizontal')

    a = fig.add_subplot(1, 2, 2)
    imgplot = plt.imshow(lum_img, cmap='gray')
    imgplot.set_clim(0.0, 175)
    a.set_title('After')
    plt.colorbar(ticks=[25, 75, 125, 175], orientation='horizontal')

    print(title)
    plt.tight_layout()
    plt.show()

def parse_cmdline():
    import argparse

    #-------------------------------------------------------------------------#
    # define args and parse them

    parser = argparse.ArgumentParser(description=
        'Playing with images by manipulating them.'
    )

    help = 'Defines which manipulations should be executed. '
    help += 'Possible values are {}'.format(CONSTANTS['tasks'])
    parser.add_argument('-t', '--tasks',
        metavar=('TASK'),
        choices=CONSTANTS['tasks'],
        nargs='+',
        default=None,
        required=True,
        help=help
    )

    args = parser.parse_args()

    #-------------------------------------------------------------------------#
    # finalize and return

    params = {}

    params['tasks'] = args.tasks

    return params

def run(params):
    '''
    Show examples of working with images.
    '''

    img = plt.imread(CONSTANTS['paths']['imgs']['orig'])

    for task in params['tasks']:
        if task == 'all':
            plot_rgba_colored(img)
            plot_rgba_grayscale(img)
            plot_YCbCr(img)
            plot_cmaps(img)
            plot_hist(img)
            plot_climmed(img)
        if task == 'rgba-colored':
            plot_rgba_colored(img)
        if task == 'rgba-grayscale':
            plot_rgba_grayscale(img)
        if task == 'YCbCr':
            plot_YCbCr(img)
        if task == 'cmaps':
            plot_cmaps(img)
        if task == 'histogram':
            plot_hist(img)
        if task == 'climmed':
            plot_climmed(img)

if __name__ == '__main__':
    params = parse_cmdline()
    run(params)
