from jira import JIRA
#from atlassian import Jira, Confluence, Bitbucket, ServiceDesk
import pandas as pd

jira = JIRA(basic_auth=('***', '***'), options={'server': 'https://itrack.web.att.com'})

issue_list = jira.search_issues('project = AICDEFECT and status = Accepted and Severity = "Severity 2"', maxResults=None)

Issue_Key = []
Project_Name = []
Issue_Type = []
Reporter = []
Status = []
Priority = []
Summary = []
Assignee = []
Created = []

for x in issue_list:
        Issue_Key.append(x)
        Project_Name.append(x.fields.project.name)
        Issue_Type.append(x.fields.issuetype.name)
        Reporter.append(x.fields.reporter)
        Assignee.append(x.fields.assignee)
        Status.append(x.fields.status.name)
        Priority.append(x.fields.customfield_10552)
        Created.append(x.fields.created)
        Summary.append(x.fields.summary)

dict1 = {'Issue_Key': Issue_Key, 'Project_Name': Project_Name, 'Issue_Type': Issue_Type, 'Reporter': Reporter, 'Status': Status, 'Priority': Priority, 'Summary': Summary, 'Assignee': Assignee, 'Created': Created}
iTrackJiraIssues = pd.DataFrame(dict1)
print(iTrackJiraIssues)

