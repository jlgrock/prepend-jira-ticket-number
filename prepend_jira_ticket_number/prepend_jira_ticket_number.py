#!/usr/local/bin/python

import argparse
import subprocess
import re

def write_output_file(msgfile, prefix):
    """reads the file, appends the prefix, and writes it out"""
    with open(msgfile) as f:
        contents = f.read()

    with open(msgfile, 'w') as f:
        f.write(prefix)
        f.write(contents)

def process_git_branch():
    """execute a git command to get the branch name"""
    git_cmd = "git symbolic-ref --short HEAD"
    output = subprocess.run(git_cmd, shell=True, capture_output=True, check=True, text=True)
    return output.stdout

def create_prepend_string(branch_name):
    """extract the jira number from the git branch name and return all matches as an array"""
    return_val = ""
    matches = re.findall('[A-Z]{3,}-[0-9]+', branch_name)
    for match in matches:
        return_val = return_val + "JIRA: [" + match + "]\n"
    return return_val

def main():
    parser = argparse.ArgumentParser(
        description='Prepend a JIRA Number to the commit message, parsed from the branch name in git.')
    parser.add_argument('-b', '--branches-to-skip', dest='branch_names_to_skip',
                        default='main,master,develop,test', metavar="branch_names",
                        help='a comma delimited list of the branches to skip - e.g. "master, develop, test"')
    parser.add_argument('git_vars', metavar='git_vars', type=str, nargs='*', help='the precommit variables')

    args = parser.parse_args()
    branches_to_skip = args.branch_names_to_skip.split(",")
    commit_msg_file = args.git_vars[0]

    branch_name = process_git_branch()
    if branch_name not in branches_to_skip:
        prefix = create_prepend_string(branch_name)
        write_output_file(commit_msg_file, prefix)

if __name__ == '__main__':
    main()


