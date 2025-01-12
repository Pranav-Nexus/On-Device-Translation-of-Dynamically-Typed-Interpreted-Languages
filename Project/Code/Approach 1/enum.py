#!/usr/bin/python
# -*- coding: utf-8 -*- 

class Enum:
    @staticmethod
    def enum(*sequential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        reverse = dict((value, key) for key, value in enums.items())
        enums['reverse_mapping'] = reverse
        return type('Enum', (), enums)