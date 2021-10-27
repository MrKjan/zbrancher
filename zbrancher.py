#! /usr/bin/env python3
# Task description
# Example input:  'https://jira.company.com/jira/browse/TASK-11111' 'Bug description'
# Example output: 'feature/PROJECT_PREFIX/TASK-11111_Bug_description'

import sys

prefix = 'PROJECT_PREFIX'

if __name__ == '__main__':
    cnt_args = len(sys.argv)

    if len(sys.argv) < 3:
        print(f"Not enough arguments. Expected: 2, found: {len(sys.argv) - 1}")
        exit()
    if len(sys.argv) > 3:
        print(f"Too much arguments. Last {len(sys.argv) - 3} arguments will be ignored")

    jira = sys.argv[1]
    bug = sys.argv[2]
    result = f"feature/{prefix}/" + jira.split('/')[-1] + "_" + bug.replace(" ", "_")

    print(result)
