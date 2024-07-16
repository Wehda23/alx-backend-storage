#!/usr/bin/env python3
"""
Changing School Topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Change name of topic based on name

    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
