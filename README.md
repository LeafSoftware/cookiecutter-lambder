This is a cookiecutter template used to create Lambder projects. It will
create the framework you can use to create new AWS Lambdas which can be
scheduled by Lambder.

REQUIRES:
* cookiecutter (https://github.com/audreyr/cookiecutter)

You can create new Lambder project with cookiecutter:

    cookiecutter cookiecutter-lambder

But the best way is to just use the lambder command in [python-lambder](https://github.com/LeafSoftware/python-lambder):

    lambder function create --name foo --bucket mybucket

See the Lambder README for more details.
