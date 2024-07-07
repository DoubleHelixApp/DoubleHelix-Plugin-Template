# DoubleHelix-Plugin-Template
>**NOTE**: At the moment this template is only used internally. DoubleHelix doesn't currently have a stable API and doesn't support any plug-in.

This templates allow to create and publish a plug-in for DoubleHelix.

## How to use the template
To use this template you need [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/). Follow its documentation to install it.

The template will also create a `git` repository configure with the repository provided during the execution of `cookiecutter`. The repository will have a `First commit` with all the file committed. Please ensure you've `git` under `PATH`.

Once `cookiecutter` is installed, use this template with:
```
cookiecutter gh:DoubleHelixApp/DoubleHelix-Plugin-Template
```

If you're using [pipx](https://github.com/pypa/pipx) and you don't have pipx executable path under `PATH` you may need to prepend `pipx run` to the command.

Follow the interactive questionnaire to configure the plugin and start developing. The code needs to be under `helix/plugins/<your-plugin-name>`.

If the `repository` var configured in cookiecutter exists and you have permission to commit there, at this point you can commit the changes with:
```
git push -u origin main
```

## How to publish the plugin
- Create an account on [PyPI](https://pypi.org/) and log-in.
- Open [this](https://pypi.org/manage/account/publishing/) page.
- Under `Add a new pending publisher` configure as follow:
    - **PyPI Project Name**: `doublehelix-<your-plugin-name>`
    - **Owner**: the username of the account that contains this repo
    - **Repository Name**: the name of the repo containing this plugin
    - **Worklfow name**: `python-publish.yml`

You're all set! Creating a new release will trigger the GitHub workflow to build and publish the plugin on PyPI. Once published, you'll be able to see your package at the address `https://pypi.org/project/doublehelix-<your-plugin-name>`. The plug-in will be installable with:

```
pip install doublehelix-<your-plugin-name>
```

Please use [semantic versioning](https://semver.org/) when creating a label.

## How to add the plug-in to the DoubleHelix plugin repository

To be done.