from jira import JIRA
from atlassian import Jira, Confluence, Bitbucket, ServiceDesk
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
Severity = []
Defect_Type = []
Blocking = []
Phase_Found_In = []
Program = []
Assigned_To_Role = []
Created = []
Detected_In_Release = []
Planned_Closing = []
PMT = []
Environment_Defects = []
Application_Found_In = []
Application_Found_In_Sub_Team = []
Created_By = []

for x in issue_list:
        Issue_Key.append(x)
        Project_Name.append(x.fields.project.name)
        Issue_Type.append(x.fields.issuetype.name)
        Reporter.append(x.fields.reporter)
        Assignee.append(x.fields.assignee)
        Status.append(x.fields.status.name)
        Priority.append(x.fields.priority.name)
        Created.append(x.fields.created)
        Summary.append(x.fields.summary)
        Severity.append(x.fields.customfield_10307)
        Defect_Type.append(x.fields.customfield_10815)
        Blocking.append(x.fields.customfield_10817)
        Phase_Found_In.append(x.fields.customfield_10822)
        Program.append(x.fields.customfield_10824)
        Assigned_To_Role.append(x.fields.customfield_10831)
        Detected_In_Release.append(x.fields.customfield_11300)
        Planned_Closing.append(x.fields.customfield_11302)
        PMT.append(x.fields.customfield_11305)
        Environment_Defects.append(x.fields.customfield_11404)
        Application_Found_In.append(x.fields.customfield_11406)
        Application_Found_In_Sub_Team.append(x.fields.customfield_11411)
        Created_By.append(x.fields.customfield_11800)

dict1 = {'Issue_Key': Issue_Key, 'Project_Name': Project_Name, 'Issue_Type': Issue_Type, 'Reporter': Reporter, 'Status': Status, 'Priority': Priority, 'Summary': Summary, 'Assignee': Assignee, 'Severity': Severity, 'Defect_Type':Defect_Type,'Blocking':Blocking,'Phase_Found_In':Phase_Found_In,'Program':Program,'Assigned_To_Role':Assigned_To_Role,'Created':Created, 'Detected_In_Release':Detected_In_Release,'Planned_Closing':Planned_Closing,'PMT':PMT,'Environment_Defects':Environment_Defects,'Application_Found_In':Application_Found_In, 'Application_Found_In_Sub_Team': Application_Found_In_Sub_Team, 'Created_By': Created_By}
JiraIssues = pd.DataFrame(dict1)
print(JiraIssues)

