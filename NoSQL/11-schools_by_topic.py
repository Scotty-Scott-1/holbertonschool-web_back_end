
#!/usr/bin/env python3
"""A module that returns specific schools"""


def schools_by_topic(mongo_collection, topic):
    """Find only the schools that have a specific topic"""

    result = mongo_collection.find(
            {"topics": topic}
    )
    return result
