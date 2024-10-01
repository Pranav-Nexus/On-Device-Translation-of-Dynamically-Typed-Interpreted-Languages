#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import copy
import os
import sys

def length_conversion():
    units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches']
    conversion_to_meters = {
        'meters': 1, 'kilometers': 1000, 'centimeters': 0.01, 'millimeters': 0.001,
        'miles': 1609.34, 'yards': 0.9144, 'feet': 0.3048, 'inches': 0.0254
    }

    while True:
        print('\nLength Conversion')
        print('Available units: meters, kilometers, centimeters, millimeters, miles, yards, feet, inches')

        try:
            value = float(input('Enter the value to convert: '))
            from_unit = input('Enter the unit to convert from: ').strip().lower()
            to_unit = input('Enter the unit to convert to: ').strip().lower()

            if from_unit not in conversion_to_meters or to_unit not in conversion_to_meters:
                print('Invalid units. Please try again.')
                continue

            result = convert_length(value, from_unit, to_unit, conversion_to_meters)

            if result is not None:
                print(f'{value} {from_unit} is equal to {result} {to_unit}')
            else:
                print('Conversion error. Please check your units and try again.')

            another_conversion = input('Do you want to perform another conversion? (yes/no): ').strip().lower()
            if another_conversion != 'yes':
                print('Exiting the program. Goodbye!')
                break

        except ValueError:
            print('Invalid input. Please enter numerical values.')

def convert_length(value, from_unit, to_unit, conversion_to_meters):
    # Convert from the initial unit to meters
    value_in_meters = np.dot(value, conversion_to_meters[from_unit])

    # Convert from meters to the target unit
    converted_value = np.dot(value_in_meters, 1 / conversion_to_meters[to_unit])

    return converted_value

length_conversion()
