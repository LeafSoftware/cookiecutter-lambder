This is a cookiecutter template used to create Lambder projects. It will
create the framework you can use to create new AWS Lambdas which can be
scheduled by Lambder.

REQUIRES:
* cookiecutter (https://github.com/audreyr/cookiecutter)

You can create a new Lambder project with cookiecutter:

    cookiecutter https://github.com/LeafSoftware/cookiecutter-lambder

But the best way is to just use the lambder command from [python-lambder](https://github.com/LeafSoftware/python-lambder):

    lambder function create --name foo --bucket mybucket

See the [python-lambder README](https://github.com/LeafSoftware/python-lambder/blob/master/README.md) for more details.
