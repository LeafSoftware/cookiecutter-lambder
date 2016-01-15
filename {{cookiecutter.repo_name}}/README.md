{{cookiecutter.repo_name}}
--------------------------

{{cookiecutter.lambda_name}} is an AWS Lambda function for use with Lambder.

REQUIRES:
* aws-cli
* virtualenvwrapper

To first setup your project:

    ./setup

Source the environment file.

    source .env

To test your lambda locally:

    ./run

To create or update your lambda code:

    ./deploy

Using virtualenvwrapper
-----------------------

Your lambdas should be as small as possible to reduce spinup time. If you need
to include extra python modules, use the virtualenv created by the setup script.
The deploy script will look for a site-packages directory in
$WORKON_HOME/{{cookiecutter.repo_name}} and bundle those packages into the zip
it uploads to AWS Lambda.
