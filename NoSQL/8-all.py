#!/usr/bin/env python3
"""A module with a function that lists all the documents"""


def list_all(mongo_collection):
    """List all documents"""

    documents = []
    cursor = mongo_collection.find()

    for doc in cursor:
        documents.append(doc)
    return documents
