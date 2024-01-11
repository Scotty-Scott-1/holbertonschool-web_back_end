#!/usr/bin/env python3
"""A module that prints stats about a db"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    result = nginx_collection.count_documents({})

    gets = nginx_collection.count_documents({"method": "GET"})
    posts = nginx_collection.count_documents({"method": "POST"})
    puts = nginx_collection.count_documents({"method": "PUT"})
    patches = nginx_collection.count_documents({"method": "PATCH"})
    deletes = nginx_collection.count_documents({"method": "DELETE"})
    status = nginx_collection.count_documents(
            {"method": "GET", "path": "/status"}
    )

    print("{} logs".format(result))
    print("Methods:")
    print("\tmethod GET: {}".format(gets))
    print("\tmethod POST: {}".format(posts))
    print("\tmethod PUT: {}".format(puts))
    print("\tmethod PATCH: {}".format(patches))
    print("\tmethod DELETE: {}".format(deletes))
    print("{} status check".format(status))
