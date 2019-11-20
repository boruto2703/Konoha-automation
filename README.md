# Creating test suites

Application web URL: http://localhost:8000

# Test Case (TC) definitions

### LOGIN case

Username: support@softagram.com | Password: Localsupport1

| TC_id | TC Name | Description |
| --- | --- | --- |
|TC_L_001| Login page successful loaded ||
|TC_L_002| Login successfully | Login successfully with correct email + password |
|TC_L_003| Login failed  | Login successfully with wrong email + password |
|TC_L_004| Reset password | Reset password worked with correct email |

### TEAM PAGE(ADMIN) cases

| TC_id | TC Name | Description |
| --- | --- | --- |
|TC_TP_001| Team page successful loaded | All team item shown, no 401 error |
|TC_TP_002| Successfully create new team (if applicable) | Superuser could create new team (not necessary)|
|TC_TP_003| Settings work | Settings page works properly to edit feild and save (not yet implement) |

### PROJECT PAGE (ADMIN) cases

| TC_id | TC Name | Description |
| --- | --- | --- |
|TC_PP_001| Load | |
|TC_PP_002| Create new project | |
|TC_PP_003| Delete | Test delete btn on project item|
|TC_PP_004| Create new project and delete | Test delete btn in repos page |
|TC_PP_005| Open, edit and save Settings | |
|TC_PP_006| Clone Settings | Clone settings from projects within a team, only if there's more than 2 projects|

```
refactor: open_settings(), login()
```

### REPO PAGE (ADMIN) cases

| TC_id | TC Name | Description |
| --- | --- | --- |
|TC_RP_001| Add (github)| Add GH repositories |
|TC_RP_002| Add (bitbucket)| |
|TC_RP_003| Add (gitlab)| |
|TC_RP_004| Add (gerrit)| |
|TC_RP_005| Add (devops)| |
|TC_RP_006| Add (BB server)| |
|TC_RP_007| Add (gitlab self-hosted)| |
|TC_RP_008| Delete repo| Delete one repo |

### ANALYSE cases

In these cases, 

first a pull request must be created (*how to create a PR automatically?*) 

and then (*test in analyse container?*)