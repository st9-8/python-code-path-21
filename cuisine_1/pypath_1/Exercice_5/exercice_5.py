#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cuboide(x,y,z,n):
    return [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print(cuboide(2,4,5,8))