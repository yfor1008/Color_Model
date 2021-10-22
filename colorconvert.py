#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# @File   : colorconvert.py
# @Author : yuanwenjin
# @Mail   : xxxx@mail.com
# @Date   : 2021/10/22 18:50:18
# @Docs   : 颜色转换相关类
'''

import numpy as np
from numpy.lib.function_base import bartlett

class ColorConvert:

    def rgb2hsv(self, rgb):
        '''
        ### Docs: rgb 转 hsv
        ### Args:
            - rgb: H*W*3, np.array, rgb 数据, [0,255]
        ### Returns:
            - hsv: H*W*3, np.array, hsv 数据, [0,1]
        '''

        rgb = rgb.astype('float') / 255
        Heigh, Width, _ = rgb.shape

        R = rgb[:,:,0]
        G = rgb[:,:,1]
        B = rgb[:,:,2]

        Cmax = np.zeros(R.shape)
        Cmin = np.zeros(R.shape)

        for row in range(Heigh):
            for col in range(Width):
                Cmax[row, col] = max(rgb[row, col, :])
                Cmin[row, col] = min(rgb[row, col, :])

        D = Cmax - Cmin

        H = np.zeros(R.shape)
        for row in range(Heigh):
            for col in range(Width):

                if D[row, col] != 0:
                    if Cmax[row, col] == R[row, col]:
                        H[row, col] = (G[row, col] - B[row, col]) / D[row, col]
                    elif Cmax[row, col] == G[row, col]:
                        H[row, col] = (B[row, col] - R[row, col]) / D[row, col] + 2
                    elif Cmax[row, col] == B[row, col]:
                        H[row, col] = (R[row, col] - G[row, col]) / D[row, col] + 4
        H = H / 6
        H[H < 0] = H[H < 0] + 1

        S = D / Cmax
        S[Cmax == 0] = 0

        V = Cmax

        hsv = np.dstack((H, S, V))

        return hsv

    def hsv2rgb(self, hsv):
        '''
        ### Docs: hsv 转 rgb
        ### Args:
            - hsv: H*W*3, np.array, hsv 数据, [0,1]
        ### Returns:
            - rgb: H*W*3, np.array, rgb 数据, [0,255]
        '''

        Height, Width, _ = hsv.shape

        H = hsv[:,:,0]
        S = hsv[:,:,1]
        V = hsv[:,:,2]

        H = H * 6
        I = np.floor(H)
        F = H - I

        M = V * (1 - S)
        N = V * (1 - S * F)
        K = V * (1 - S * (1 - F))

        rgb = np.zeros(hsv.shape)
        for row in range(Height):
            for col in range(Width):
                if I[row, col] == 0:
                    rgb[row, col, :] = (V[row, col], K[row, col], M[row, col])
                elif I[row, col] == 1:
                    rgb[row, col, :] = (N[row, col], V[row, col], M[row, col])
                elif I[row, col] == 2:
                    rgb[row, col, :] = (M[row, col], V[row, col], K[row, col])
                elif I[row, col] == 3:
                    rgb[row, col, :] = (M[row, col], N[row, col], V[row, col])
                elif I[row, col] == 4:
                    rgb[row, col, :] = (K[row, col], M[row, col], V[row, col])
                elif I[row, col] == 5:
                    rgb[row, col, :] = (V[row, col], M[row, col], N[row, col])

        rgb = np.round(rgb * 255)

        return rgb

if __name__ == '__main__':

    import scipy.io as scio

    cvt = ColorConvert()

    rgb = np.random.randint(0,255, size=(16,16,3))
    # rgb = np.zeros((1,1,3))
    # rgb[0, 0, 0] = 209
    # rgb[0, 0, 1] = 52
    # rgb[0, 0, 2] = 52
    hsv = cvt.rgb2hsv(rgb)
    rgb1 = cvt.hsv2rgb(hsv)
    scio.savemat('hsv.mat', {'hsv': hsv, 'rgb': rgb, 'rgb1': rgb1})

    print((rgb == rgb1).all())
    # if not (rgb == rgb1).all():
    #     print(rgb)
    #     print('++++++++++++')
    #     print(rgb1)
    #     print('++++++++++++')
    #     print(rgb - rgb1)


