# DoubleHelix-Plugin-Template
*NOTE*: At the moment this template is only used internally. DoubleHelix doesn't currently have a stable API and doesn't support any plug-in.

This templates allow to create and publish a plug-in for DoubleHelix.

## How to use the template
To use this template you need [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/). Follow its documentation to install it.

Once installed, use this template with:
```
cookiecutter gh:DoubleHelixApp/DoubleHelix-Plugin-Template
```

If you're using [pipx](https://github.com/pypa/pipx) and you don't have pipx executable path under PATH you may need to prepend `pipx run` to the command.

Follow the interactive questionnaire to configure the plugin and start developing. The code needs to be under helix/plugins/<your-plugin-name>.

## How to publish the plugin
- Create an account on [PyPI](https://pypi.org/).
- On PyPI, under `Publishing` fill the information in the section `Add a new pending publisher`:
    - PyPI Project Name: the name how you want your plug-in to appear on PyPI
    - Owner: the username of the account that contains this repo
    - Repository Name: the name of the repo containing this plugin
    - Worklfow name: `python-publish.yml`

You're all set! Create a new release and enjoy the magic.

## How to add the plu-in to the DoubleHelix plugin repository

To be done.