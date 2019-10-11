#-*- coding: utf-8 -*-
import cv2
import numpy as np
img = cv2.imread('F:/python/image/bookpage.jpg')
#retval ,threshold = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY)

grayscled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval_1,threshold_1 = cv2.threshold(grayscled, 130, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 107, 1)
"""
    adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
    .   @brief Applies an adaptive threshold to an array.
    .   
    .   The function transforms a grayscale image to a binary image according to the formulae:
    .   -   **THRESH_BINARY**
    .   \f[dst(x,y) =  \fork{\texttt{maxValue}}{if \(src(x,y) > T(x,y)\)}{0}{otherwise}\f]
    .   -   **THRESH_BINARY_INV**
    .   \f[dst(x,y) =  \fork{0}{if \(src(x,y) > T(x,y)\)}{\texttt{maxValue}}{otherwise}\f]
    .   where \f$T(x,y)\f$ is a threshold calculated individually for each pixel (see adaptiveMethod parameter).
    .   
    .   The function can process the image in-place.
    .   
    .   @param src Source 8-bit single-channel image.
    .   @param dst Destination image of the same size and the same type as src.
    .   @param maxValue Non-zero value assigned to the pixels for which the condition is satisfied
    .   @param adaptiveMethod Adaptive thresholding algorithm to use, see #AdaptiveThresholdTypes.
    .   The #BORDER_REPLICATE | #BORDER_ISOLATED is used to process boundaries.
    .   @param thresholdType Thresholding type that must be either #THRESH_BINARY or #THRESH_BINARY_INV,
    .   see #ThresholdTypes.
    .   @param blockSize Size of a pixel neighborhood that is used to calculate a threshold value for the
    .   pixel: 3, 5, 7, and so on.
    .   @param C Constant subtracted from the mean or weighted mean (see the details below). Normally, it
    .   is positive but may be zero or negative as well.
    .   
    .   @sa  threshold, blur, GaussianBlur
    """




retval_2, otsu = cv2.threshold(grayscled, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imshow('original',img)
#cv2.imshow('threshold',threshold)
#cv2.imshow('grayscled',grayscled)
#cv2.imshow('threshold_1',threshold_1)
cv2.imshow('gaus', gaus)
cv2.imshow('otsu', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()