from jira import JIRA
from atlassian import Jira
from atlassian import Confluence
from atlassian import Bitbucket
from atlassian import ServiceDesk
import pandas as pd

jira = JIRA(basic_auth=('***', '***'), options={'server': 'https://jira.web.labs.att.com'})

jiraquery = 'project = defect and "Defect Type" = Issue and status = "Open / In Analysis" and severity = "Severity 2"'
jiraquery = jiraquery.replace("\"", "'")

issue_list = jira.search_issues(jiraquery, maxResults=None)

Issue_Key = []
AllLabels = []

for ticket in issue_list:
    issue = jira.issue(ticket)
    labels = issue.fields.labels
    for i in labels:
        Issue_Key.append(ticket)
        AllLabels.append(i)

dict1 = {'Issue_Key': Issue_Key, 'AllLabels': AllLabels}
JiraLabels = pd.DataFrame(dict1)
print(JiraLabels)

