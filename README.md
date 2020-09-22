# LabWebsite

The website for the UIUC Learning and Language Lab is under git version control.
It is a static website built in the [hugo ](https://gohugo.io/) framework and uses the [foundations](https://themes.gohugo.io/foundation-theme/) theme.

It is accessible via the domains:
* [learninglanguagelab.com](http://learninglanguagelab.com) (registered with godaddy.com)
* [learninglanguagelab.org](http://learninglanguagelab.org) (registered with godaddy.com)
* [languagelearninglab.org](http://languagelearninglab.org) (registered with weebly.com)

It is hosted at `incommesurable.com/lab_website` (registered with godaddy.com).

## Updating

To update the website:
* clone the repository
* make changes
* compile using `hugo`
* make sure any added files are added to Git Version Control 
* simply push the changes to Github, which will trigger a deployment script that copies the content of `built_by_hugo` to incommesurable.com

Check the status of the website build by clicking on the `Actions` tab on the Github browser interface. 

## Automatic Deployment

Automatic deployment on a push to Github is made possible by Github Actions. 
The action which performs the atuomatic deployment can be configured by editing `workflow.yml` in `.github`
