CHANGELOG = 'CHANGELOG.md'
arguments = {}


def common_arguments():
    """
    Return common arguments

    :return: tuple of <app_name>, --dry-run, new_version
    """

    app_name = arguments['<app_name>']

    version_prefix = arguments.get('--version-prefix')
    new_version = arguments['new_version']

    common_arguments = (
        app_name,
        arguments['--dry-run'],
        version_prefix + new_version if version_prefix else new_version,
    )
    return common_arguments