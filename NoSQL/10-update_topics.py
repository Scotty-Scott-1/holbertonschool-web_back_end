#!/usr/bin/env python3
"""A module that updated docuemnts"""


def update_topics(mongo_collection, name, topics):
    """Insert a document"""

    result = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
    return result
