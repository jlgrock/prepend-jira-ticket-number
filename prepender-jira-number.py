#!/usr/local/bin/python

import argparse
import subprocess
import re

parser = argparse.ArgumentParser(
    description='Prepend a JIRA Number to the commit message, parsed from the branch name in git.')
parser.add_argument('-b', '--branches-to-skip', dest='branch_names_to_skip',
                    default='main master develop test', metavar="branch_names",
                    help='a comma delimited list of the branches to skip - e.g. "master, develop, test"')
parser.add_argument('commit_messages', metavar='commit_message', type=str, nargs='*',
                    help='the commit message to accept')
args = parser.parse_args()

try:
    branches_to_skip = args.branch_names_to_skip.split(",")
except:
    raise Exception("There is a problem with the branch names to skip in the prepend-jira-ticket-number pre-commit hook.")

commit_message = ""
if args.commit_messages is not None:
    if len(args.commit_messages) > 0:
        commit_message = args.commit_messages[0]

git_cmd = "git symbolic-ref --short HEAD"
output = subprocess.run(git_cmd, shell=True, capture_output=True, check=True, text=True)
branch = output.stdout

stdout = ""
if branch not in branches_to_skip:
    print("branch: " + output.stdout)

    matches = re.findall('[A-Z]{3,}-[0-9]+', output.stdout)
    for match in matches:
        stdout = stdout + "JIRA: [" + match + "]\n"

stdout = stdout + commit_message
print(stdout)
