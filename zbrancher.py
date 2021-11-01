#! /usr/bin/env python3
# Task description
# Example input:  'https://jira.company.com/jira/browse/TASK-11111' 'Bug description'
# Example output: 'feature/PROJECT_PREFIX/TASK-11111_Bug_description'

import sys
import configparser

names = {
    "task_prefix": "TASK",
    "project_prefix": "PROJECT_PREFIX",
    "branch_type": "feature",
    "branch_type_bug": "bugfix",
    }

settings = {
    "task_format": "link",
}

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')

    names = {**names, **config['NAMES']}
    settings = {**settings, **config['SETTINGS']}

    task_prefix = names['task_prefix']
    project = names['project_prefix']
    type = names['branch_type']

    cnt_args = len(sys.argv)
    if cnt_args < 3:
        print(f"Not enough arguments. Expected: 2, found: {cnt_args - 1}")
        exit()
    if cnt_args > 3:
        print(f"Too much arguments. Last {cnt_args- 3} arguments will be ignored")

    task = sys.argv[1]
    description = sys.argv[2]

    if settings["task_format"] == 'link':
        task = task.split('/')[-1]
    elif settings["task_format"] == 'number':
        task = f"{task_prefix}_{task}"

    description = description.replace(' ', '_')
    result = f"{type}/{project}/{task}_{description}"

    print(result)
