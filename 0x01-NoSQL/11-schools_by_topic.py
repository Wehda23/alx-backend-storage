#!/usr/bin/env python3
"""
School Topics
"""


def schools_by_topic(mongo_collection, topic):
    """
    Grabs Topics

    :param mongo_collection:
    :param topic:
    :return:
    """
    return mongo_collection.find({"topics": topic})
