#!/usr/bin/env python3
"""
module doc
"""


def insert_school(mongo_collection, **kwargs):
    """
    function documentation
    """
    return mongo_collection.insert_one(kwargs).inserted_id
