from jira import JIRA
from atlassian import Jira, Confluence, Bitbucket, ServiceDesk
import pandas as pd

jira = JIRA(basic_auth=('***', '***'), options={'server': 'https://itrack.web.att.com'})
issue_list = jira.search_issues("project = CPDEFECT AND 'Phase Found In' = 'Integrated Systems Test (IST)' AND 'Application Found In' ~ NC:29002 AND Severity in ('Severity 1', 'Severity 2') AND updated > startOfMonth(-1M) AND updated < startOfMonth() AND 'Defect Type' = Defect AND created > startOfMonth(-1M) AND created < startOfMonth() AND status = Accepted", maxResults=None)

Issue_Key = []
Created = []
Field = []
From = []
To = []
Author = []
ik = ""
histc = ""
itmf = ""
itmfrm = ""
itmto = ""
histauth = ""
flag = 0

for x in issue_list:
    issue = jira.issue(x.key, expand='changelog')
    changelog = issue.changelog
#    print(x.key)
    for history in changelog.histories:
        for item in history.items:
            if item.field == 'status' and item.toString == 'Test Complete':
#                print(issue.key + ' Date:' + history.created + ' From:' + item.fromString + ' To:' + item.toString)
#                print(history.author)
                ik = issue.key
                histc = history.created
                itmf = item.field
                itmfrm = item.fromString
                itmto = item.toString
                histauth = history.author
                flag = 1
            elif flag == 0 and item.field == 'status' and item.toString == 'Accepted':
                ik = issue.key
                histc = history.created
                itmf = item.field
                itmfrm = item.fromString
                itmto = item.toString
                histauth = history.author
                flag = 1

    Issue_Key.append(ik)
    Created.append(histc)
    Field.append(itmf)
    From.append(itmfrm)
    To.append(itmto)
    Author.append(histauth)
    flag = 0


dict1 = {'Issue_Key': Issue_Key, 'Created': Created, 'Field': Field, 'From': From, 'To': To, 'Author': Author}
ChangeLog = pd.DataFrame(dict1)
print(ChangeLog)

