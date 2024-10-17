# ** Document Consultancy Services (DCS)**

DCS is an online platform that offers various document drafting services including property, legal etc.
It is a comprehensive web-based platform for documents consultancy services that will allow users to draft and manager a wide range of documents related to property transactions, rentals, agreements and affidavits.

Folder structure:

- backend/: Contains the server-side code, configuration files, and related resources.
- frontend/: Contains the client-side code, assets, and build configurations.
- .gitignore: Specifies files and directories that should be ignored by Git.

## Branch Strategies ##

- main: Latest development changes.
- release: Stable production code, which will be used for deployment purpose.
- Feature branches: Created for new features or fixes and merged into main via pull requests.
- Branch naming Conventions: {feature-name} eg: feature-frontend, feature-backend, feature-templates etc..

Managing Secrets (if using GitHub Actions):
- Add and manage secrets under Settings → Secrets and Variables to store sensitive information like API keys, AWS credentials, etc.

Github actions and workflows:

Workflows are defined in .yaml files stored in the .github/workflows/ directory in the repository.
Following actions configured to automate build, test and deployment processes by running predefined tasks on events like code pushes or pull requests.
- ci.yml : The workflow triggers on pushes and pull requests to the main branch. Upon successful build it checks-in to release branch.

To optimize workflow, caching dependencies enabled to speed up builds.

Managing Secrets, under GitHub Secrets, AWS access key credentials stored.
- -name: Set up AWS credentials
   - run: aws configure set aws_access_key_id ${{ secrets.AWS_ACCESS_KEY_ID }}.



