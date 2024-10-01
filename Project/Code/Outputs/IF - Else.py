#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import copy
import os
import sys

def checkNumber(num):

    if num > 0:
        result = 'Thenumberispositive.'
    elif num < 0:
        result = 'Thenumberisnegative.'
    else:
        result = 'Thenumberiszero.'


    return result

