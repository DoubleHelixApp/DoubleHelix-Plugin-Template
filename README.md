# DoubleHelix-Plugin-Template
*NOTE*: At the moment this template is only used internally. DoubleHelix doesn't currently have a stable API and doesn't support any plug-in.

This templates allow to create and publish a plug-in for DoubleHelix.

## How to use the template
To use it, click on the button on the top-right, `Use this template`:
- Import the project in another repository
- Modify the `pyproject.toml` . Look for the tag `<fillme>` and supply the necessary information.
- Add or remove any tags or classifier
- Please maintain the convention used in the `pyproject.toml` file or the plug-in may not be accepted in the repository. Specifically, the name of the package on PyPI should be `doublehelix-<pluginname>`.
- Start developing! Be aware the code for the plug-in needs to be under the namespace `doublehelix.plugins` in order for DoubleHelix to find it.

## Developing
Follow the instruction to install [DoubleHelix](https://doublehelix.app). Add your code under `helix/plugins/<pluginname>`.

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