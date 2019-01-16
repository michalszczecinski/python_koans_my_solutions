#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle_prev(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    if (a <= 0) or (b<=0) or (c<=0):
        raise TriangleError("All sides should be positive")
    elif (a +b <c) or (b+c<a) or (c+a<b): 
        raise TriangleError("Sum of two sides should be greater than 3rd one")
    else:
        if a == b == c:
        	return 'equilateral'
        elif (a==b) or (a==c) or (b==c):
        	return 'isosceles'
        else:
        	return 'scalene'

def triangle2(a, b, c):
    # this one is another take on it using counting elements

    l = [a,b,c]
    s = set(l)
    diff = len(l) - len(s)

    if diff == 0:
    	return 'scalene'
    elif diff==1:
    	return 'isosceles'
    elif diff==2:
    	return 'equilateral'

## functions solutioons



def test_2_sides_greater_than_3rd(a,b,c):
    # smarter solution
    # because if 2 other sides are be bigger than the largest one, than this applies to all,
    # if thasts the case then sum of all should be at least twice as big as max one, because its max one + other sides
    return sum([a,b,c]) <= 2 * max(a,b,c) 


def triangle(a, b, c):
    if (a <= 0) or (b<=0) or (c<=0):
        raise TriangleError("All sides should be positive")
    elif test_2_sides_greater_than_3rd(a,b,c):
        raise TriangleError("Sum of two sides should be greater than 3rd one")
    else:
        if a == b == c:
            return 'equilateral'
        elif (a==b) or (a==c) or (b==c):
            return 'isosceles'
        else:
            return 'scalene'


# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass


