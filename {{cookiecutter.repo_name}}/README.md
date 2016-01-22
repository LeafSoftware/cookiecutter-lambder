# {{cookiecutter.repo_name}}

{{cookiecutter.lambda_name}} is an AWS Lambda function for use with Lambder.

REQUIRES:
* python-lambder

## Getting Started

1) Test the sample lambda function

    python lambda/{{cookiecutter.lambda_name}}/{{cookiecutter.lambda_name}}.py

2) Deploy the sample Lambda function to AWS

    lambder function deploy

3) Invoke the sample Lambda function in AWS

    lambder function invoke --input input/ping.json

4) Add useful code to lambda/{{cookiecutter.lambda_name}}/{{cookiecutter.lambda_name}}.py

5) Add any permissions you need to access other AWS resources to iam/policy.json

6) Update your lambda and permissions policy in one go

    lambder function deploy

## Using virtualenvwrapper

Your Lambdas should be as small as possible to reduce spinup time. If you need
to include extra python modules, use virtualenvwrapper.
The deploy script will look for a site-packages directory in
$WORKON_HOME/{{cookiecutter.repo_name}} and bundle those packages into the zip
that it uploads to AWS Lambda.
