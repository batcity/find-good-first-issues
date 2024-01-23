import subprocess
def curl_request(url):

    # Define the command to execute using curl
    command = ['curl', '-L', '-H', 'Accept: application/vnd.github+json', '-H',
     'Authorization: Bearer [token]', '-H',
      'X-GitHub-Api-Version: 2022-11-28', url]

    # Execute the curl command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    # Return the stdout of the curl command
    return result.stdout

# Make a curl request to grab open issues labeled good first issues
url = 'https://api.github.com/repos/ray-project/ray/issues'
amended_url = url + '?labels=good%20first%20issue&?state=open'

response = curl_request(amended_url)

# print the response
print(response)
