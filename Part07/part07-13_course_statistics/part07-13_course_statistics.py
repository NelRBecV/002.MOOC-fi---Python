# Write your solution here
"""
    This script worked just fine on VS code. If you have some SSL issues just do as follows:
     - import 'ssl' and 'certifi' libraries to the file.py.
     
     - assign a variable to receive the value from ssl.create_default_context(cafile=certifi.where())
       Note: certifi.where() retrieves the path where certificates files are stored on local disk.
       
     - Finally, add the recently created variable to the parameter 'context' in urllib.request.urlopen
       urllib.request.urlopen(url, context=variable)            
"""

import json
import math
import urllib.request


def retrieve_all() -> list:    
    url: str = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    data = urllib.request.urlopen(url)
    course_list = json.loads(data.read())
    courses: list = []

    for value in course_list:
        if value['enabled']:
            courses.append((value['fullName'], value['name'], value['year'], sum(value['exercises'])))

    return courses


def retrieve_course(course_name: str) -> dict:    
    url: str = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    data = urllib.request.urlopen(url)
    courses: dict = json.loads(data.read())
    course_stats: dict = {'weeks': 0, 'students': 0, 'hours': 0, 'hours_average': 0, 'exercises': 0,
                          'exercises_average': 0}
    print(courses)

    if len(courses) != 0:
        for cour, items in courses.items():
            course_stats['weeks'] += 1

            # Gets the highest number of students recorded for all weeks
            if course_stats['students'] < items['students']:
                course_stats['students'] = items['students']

            # Calcualtes total amount of hours and excercises of whole course
            course_stats['hours'] += items['hour_total']
            course_stats['exercises'] += items['exercise_total']

        # Calculates general average of hours and excercise from the course
        course_stats['exercises_average'] = math.floor(course_stats['exercises'] / course_stats['students'])
        course_stats['hours_average'] = math.floor(course_stats['hours'] / course_stats['students'])

        return course_stats


if __name__ == "__main__":
    print(retrieve_all())
    print()
    print(retrieve_course("ofs2019"))
