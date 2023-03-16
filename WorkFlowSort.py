import requests


def sort_github_workflows( token,sort_option=0,is_workflow=0 ):
    """
Sorts and filters the Workflows in your GitHub repositories based on user input.

Args:

    - token (str): Your GitHub personal access token.
    - sort_option = [by-name: 0, by-starting date: 1, by-ending-date: 2]
    - is_workflow=0,1
    
Returns:
    - The sorted dictionary of repos with starting and ending date
"""

    import requests

    # Set up the API endpoint and headers
    url = "https://api.github.com/user/repos?affiliation=owner"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {token}"
        }

    # Send the get request to the API endpoint
    repos_response = requests.get(url, headers=headers)
    # print(repos_response.status_code)
    # Prompt the user to choose a sorting option
    # while sort_option not in [1, 2, 3]:
    #     sort_option = int(input("Choose a sorting option:\n1. Sort by name\n2. Sort by starting date\n3. Sort by end date\n"))
    
    # # Prompt the user to choose a filtering option
    # while is_workflow not in [0, 1]:
    #     is_workflow = int(input("Choose a filtering option:\n0. Show repos with workflows\n1. Show repos with/without workflows\n"))
    
    # Check the status code of the response
    if repos_response.status_code == 200:
        # Successful request
        repos = repos_response.json()
        
        # print(repos)
        
        repo_times = []
        for repo in repos:
            # Get the workflow runs for the repository
            runs_url = f"https://api.github.com/repos/{repo['full_name']}/actions/runs"
            runs_response = requests.get(runs_url, headers=headers)
    
            # Check the status code of the response
            if runs_response.status_code == 200:
                # Successful request
                runs = runs_response.json()
    
                # Add the repository name, starting date, and completed date of most recent workflow run to the repo_times list
                if len(runs["workflow_runs"]) > 0:
                    repo_times.append({"repo_name": repo['name'], 
                                       "start_date": runs["workflow_runs"][0]['created_at'],
                                       "completed_date": runs["workflow_runs"][0]['updated_at']})
                elif is_workflow == 1:
                    # If the repo has no workflow runs and the user wants to show repos without workflows, add the repository name with empty start and completed dates
                    repo_times.append({"repo_name": repo['name'], "start_date": "", "completed_date": ""})
            else:
                # Failed request
                print(f"Failed to get workflow runs for {repo['name']}")
    
        # Sort the repo_times list by the chosen date/time in ascending order
        sorted_repo_times = {}
        if sort_option == 0:
            sorted_repo_times = sorted( repo_times, key=lambda x: x["repo_name"] )
        elif sort_option == 1:
            sorted_repo_times = sorted( repo_times, key=lambda x: x["start_date"] )
        elif sort_option == 2:
            sorted_repo_times = sorted( repo_times, key=lambda x: x["completed_date"] )
    
        # Print the repo names, starting dates, and completed dates in order
        for repo_time in sorted_repo_times:
            print("Repo name: {0:>30s} - starting date: {1:}, completed date: {2:}".format(repo_time['repo_name'], repo_time['start_date'], repo_time['completed_date']))
        return sorted_repo_times
    else:
        # Failed request
        print("Failed to get repositories")
        return -999

# Your GitHub personal access token
# token = 'your_token'
# c = sort_github_workflows( token,sort_option=2,is_workflow=0 )
