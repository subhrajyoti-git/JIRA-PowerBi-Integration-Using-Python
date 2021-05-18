from jira import JIRA
from atlassian import Jira, Confluence, Bitbucket, ServiceDesk
import pandas as pd

jira = JIRA(basic_auth=('***', '***'), options={'server': 'https://jira.web.labs.att.com'})

issue = jira.issue('DEFECT-26673', expand='changelog')
changelog = issue.changelog

for history in changelog.histories:
    for item in history.items:
        if item.field == 'status':
            print(issue.key + ' Date:' + history.created + ' From:' + item.fromString + ' To:' + item.toString)
#item.toString
