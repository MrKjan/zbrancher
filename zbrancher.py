#! /usr/bin/env python3
# Task description
# Example input:  'https://jira.company.com/jira/browse/TASK-11111' 'Bug description'
# Example output: 'feature/PROJECT_PREFIX/TASK-11111_Bug_description'

import configparser
import argparse

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
    parser = argparse.ArgumentParser(description='''
        Makes name of a git branch out of Jira task and its description.
        "zbrancher 'https://jira.company.com/jira/browse/TASK-11111' 'Bug description'"
        should produce
        "feature/PROJECT_PREFIX/TASK-11111_Bug_description"
        if config file is default
        ''')
    parser.add_argument('-b', action='store_true',
        help='if set, bug prefix will be written instead of default')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-l', action='store_true',
        help='task format should be: "https://jira.company.com/jira/browse/TASK-12345"')
    group.add_argument('-n', action='store_true', help='task format should be: "12345"')
    group.add_argument('-r', action='store_true', help='task format should be: "TASK-12345"')
    parser.add_argument('task')
    parser.add_argument('description')
    args = parser.parse_args()

    names = {**names, **config['NAMES']}
    settings = {**settings, **config['SETTINGS']}

    task_prefix = names['task_prefix']
    project = names['project_prefix']
    type = names['branch_type']
    if vars(args)['b']:
        type = names['branch_type_bug']


    task_format = settings['task_format']
    if vars(args)['l']:
        task_format = 'link'
    if vars(args)['n']:
        task_format = 'number'
    if vars(args)['r']:
        task_format = 'raw'

    task = vars(args)['task']
    description = vars(args)['description']

    if task_format == 'link':
        task = task.split('/')[-1]
    elif task_format == 'number':
        task = f"{task_prefix}_{task}"

    description = description.replace(' ', '_')
    result = f"{type}/{project}/{task}_{description}"

    print(result)
