import asana


# Paste here your asana access token
ACCESS_TOKEN = ""

client = asana.Client.access_token(ACCESS_TOKEN)
me = client.users.me()

# Paste here the team gid from the team that you have been invited
TEAM_GID = ""
all_projects = client.projects.get_projects({"team": TEAM_GID}, opt_pretty=True)

for projects in all_projects:
    print(projects)
