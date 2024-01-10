#!/usr/bin/env python3
"""A module that inserts a document"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document"""
    return mongo_collection.insert_one(kwargs)
