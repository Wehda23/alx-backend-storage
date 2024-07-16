#!/usr/bin/env python3
"""
Grabs top students
"""


def top_students(mongo_collection):
    """
    Grabs average score of students
    :param mongo_collection:
    :return:
    """
    return mongo_collection.aggregate(
        [
            {"$project": {"name": "$name", "averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": -1}},
        ]
    )
