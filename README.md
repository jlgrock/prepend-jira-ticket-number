# Prepend-JIRA-Ticket-Link

Pre-Commit hook that prepends JIRA ticket number and URL in the commit message.

## Adding to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/jlgrock/prepend-jira-ticket-link
    rev: v0.2.0
    hooks:
    -   id: prepend-jira-link
    # ...
```

## Provided hooks

- [x] **prepend-jira-link** - Adds [JIRA](https://www.atlassian.com/software/jira) ticket number and link to commit message.
    - If JIRA ticket ID is not present in commit message, it will check the branch name, if it contains a ticket id.
    - If found will append it to the commit message.
    - 
### Example

Branch named:

```text
feature/DGT-329-updating-java-version
```

Commit message:

```shell
git commit -m"Updating Spring Boot to latest version"
```

Example Output (which can be verified via `git log`):

```
JIRA: [DGT-329]

Updating Spring Boot to latest version
```
