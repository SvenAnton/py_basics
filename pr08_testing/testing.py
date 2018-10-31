"""Test 'shortest way back' ex."""


import pytest
import shortest_way_back
import random


def test_shortest_way_back():
    assert shortest_way_back("NNN") == "SSS"

def test_west():
    assert shortest_way_back("W") == "E"

def test_east():
    assert shortest_way_back("E") == "W"
