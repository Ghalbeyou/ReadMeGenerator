import sys


def generate():
    app_name = sys.argv[1]
    git_url = sys.argv[2]
    git_owner = sys.argv[3]
    license = sys.argv[4]
    website_url = sys.argv[5]
    out_name = sys.argv[6]
    if app_name == '' or git_url == '' or git_owner == '' or license == '' or website_url == '' or out_name == '':
        help()
        return
    print("Generate!")
    file_content = f"""# {app_name}
\n\n
## Description\n\n
This app is open source. the owner of this app is [@{git_owner}](https://github.com/{git_owner}).
`Your app description here`\n\n
\n\n
App is available on [{website_url}]({website_url}) too.
\n\n
## Installation\n\n
To install this app, you can use the following command:
`your install commands here!`
\n\n
```
pip install {app_name}
```
\n\n
## Usage
```
{app_name} --help
```
\n\n
## Contributing\n\n
`This part must be edited by you!`\n\n
Please visit [{git_url}]({git_url}/) for more information.
\n\n
## License\n\n
This app is licensed under the {license} license.
\n\n
## Author\n\n
[{git_owner}](https://github.com/{git_owner})
\n\n
## Version\n\n
1.0
\n\n
## Repository\n\n
[{git_url}]({git_url})
\n\n
## Issues\n\n
`Your rules for issues here`\n\n
[Click here to send issue]({git_url}/issues)
## Contact us\n\n
If you have any questions, please contact us at [@{git_owner}](https://github.com/{git_owner})
\n\n
## End\n\n
All copyright for {git_owner} on github and his app {app_name} on github!
"""
    with open(f'{out_name}.md', "w") as f:
        f.write(file_content)

def help():
    print('Import this module and use generate function.')

generate()