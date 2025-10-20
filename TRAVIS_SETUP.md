# Travis CI Setup Guide

This guide will walk you through setting up Travis CI for your Django project step by step.

## Prerequisites

- GitHub account with your repository (https://github.com/itsSirish/swe1-app)
- AWS account with Elastic Beanstalk environment already set up

## Step 1: Set Up Travis CI Account

1. Go to [Travis CI](https://travis-ci.com/)
2. Click "Sign up with GitHub"
3. Authorize Travis CI to access your GitHub account
4. Accept the GitHub permissions

## Step 2: Activate Your Repository

1. Once logged in to Travis CI, click on your profile picture (top right)
2. Click "Settings"
3. Find your repository `itsSirish/swe1-app` in the list
4. Toggle the switch to enable Travis CI for this repository
   - If you don't see your repository, click "Sync account" button

## Step 3: Set Up Coveralls for Code Coverage

1. Go to [Coveralls.io](https://coveralls.io/)
2. Sign in with GitHub
3. Click "Add Repos"
4. Find `itsSirish/swe1-app` and toggle it ON
5. Click on your repository name to view its settings
6. Copy the repo token (you'll need this if builds fail)

## Step 4: Configure AWS Credentials in Travis

You need to add your AWS credentials as environment variables in Travis CI:

1. In Travis CI, go to your repository settings:
   - Click on your repository
   - Click "More options" (three dots) → "Settings"

2. Scroll down to "Environment Variables" section

3. Add the following environment variables:
   - Name: `AWS_ACCESS_KEY_ID`
     - Value: Your AWS Access Key ID
     - Keep "Display value in build log" OFF (for security)

   - Name: `AWS_SECRET_ACCESS_KEY`
     - Value: Your AWS Secret Access Key
     - Keep "Display value in build log" OFF (for security)

### How to Get AWS Credentials:

1. Log in to AWS Console
2. Click on your username (top right) → "Security credentials"
3. Scroll to "Access keys" section
4. Click "Create access key"
5. Download or copy the Access Key ID and Secret Access Key
   - **Important**: Save these immediately, you won't be able to see the secret key again!

## Step 5: Update .travis.yml with Your AWS Details

You need to update the [.travis.yml](.travis.yml) file with your specific AWS information:

```yaml
deploy:
  provider: elasticbeanstalk
  region: "us-east-1"  # Change to your region (e.g., us-west-2, eu-west-1)
  app: "mysite"  # Change to your EB application name
  env: "mysite-env"  # Change to your EB environment name
  bucket_name: "elasticbeanstalk-us-east-1-YOUR-ACCOUNT-ID"  # Change to your S3 bucket
```

To find these values:

1. **Region**: Check your AWS Elastic Beanstalk console - it's in the URL or displayed in the console
2. **App name**: In EB console, this is your "Application name"
3. **Env name**: In EB console, this is your "Environment name"
4. **Bucket name**: In EB console → Application → Application versions → look at S3 bucket name

## Step 6: Commit and Push Your Changes

```bash
git add .
git commit -m "Add Travis CI configuration with testing and deployment"
git push origin main
```

## Step 7: Verify Travis CI Build

1. Go to [Travis CI Dashboard](https://travis-ci.com/)
2. Click on your repository
3. You should see a build starting automatically
4. Watch the build log to see:
   - Dependencies installation
   - Black formatting check
   - Flake8 linting
   - Test execution with coverage
   - Deployment to AWS EB (if tests pass)

## Step 8: Set Up Branch Protection Rules

1. Go to your GitHub repository: https://github.com/itsSirish/swe1-app
2. Click "Settings" tab
3. Click "Branches" in the left sidebar
4. Click "Add rule" or "Add branch protection rule"
5. Configure the rule:
   - Branch name pattern: `main`
   - Check: "Require status checks to pass before merging"
   - Check: "Require branches to be up to date before merging"
   - Select these status checks:
     - `continuous-integration/travis-ci`
   - Check: "Require a pull request before merging" (optional but recommended)
6. Click "Create" or "Save changes"

## Step 9: Test with a Pull Request

1. Create a new branch:
```bash
git checkout -b test-travis
```

2. Make a small change (e.g., add a comment to a file)

3. Commit and push:
```bash
git add .
git commit -m "Test Travis CI integration"
git push origin test-travis
```

4. Go to GitHub and create a Pull Request from `test-travis` to `main`

5. You should see Travis CI automatically run checks on the PR

6. If everything passes, you'll see green checkmarks

## Troubleshooting

### Build Fails on Black Check

If the build fails because of code formatting:

```bash
# Run black locally to format your code
black .

# Commit the changes
git add .
git commit -m "Fix code formatting with black"
git push
```

### Build Fails on Flake8

If flake8 reports issues:

```bash
# Check what the issues are
flake8 .

# Fix them manually or add # noqa comments for false positives
```

### Coverage Upload Fails

If Coveralls upload fails, you may need to add the `COVERALLS_REPO_TOKEN`:

1. Get your token from Coveralls.io (repository settings)
2. Add it to Travis CI environment variables:
   - Name: `COVERALLS_REPO_TOKEN`
   - Value: Your token from Coveralls

### AWS Deployment Fails

Common issues:
- Wrong region/app name/environment name in .travis.yml
- Missing or incorrect AWS credentials
- EB environment not ready/healthy
- Insufficient IAM permissions

## Your Travis Dashboard URL

Once set up, your Travis CI dashboard will be at:
https://travis-ci.com/github/itsSirish/swe1-app

This is the URL you'll submit for your assignment!

## Verification Checklist

- [ ] Travis CI is activated for your repository
- [ ] Coveralls is activated for your repository
- [ ] AWS credentials are configured in Travis
- [ ] .travis.yml is updated with correct AWS details
- [ ] All files are committed and pushed to GitHub
- [ ] Build status badge shows in README.md
- [ ] Coverage badge shows in README.md
- [ ] Branch protection is enabled on main branch
- [ ] Pull request triggers Travis CI build
- [ ] Tests pass and app deploys to AWS EB

## Next Steps

After everything is working:
1. Add more meaningful tests to [polls/tests.py](polls/tests.py)
2. Improve code coverage
3. Add more features to your app
4. Every push will trigger Travis CI automatically!

Good luck!
