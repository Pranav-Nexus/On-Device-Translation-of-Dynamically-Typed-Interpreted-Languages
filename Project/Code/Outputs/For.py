#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import copy
import os
import sys

def calculateFactorial(n):

    result = 1
    for i = xrange(0,n):
        result = np.dot(result,i)

    return result

