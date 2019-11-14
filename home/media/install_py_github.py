#!/usr/bin/env python3
from pathlib import Path
import urllib.request
import subprocess as sp
from argparse import ArgumentParser
import re


def _version(url) -> str:
    url = f'{url}/releases/latest'
    req = urllib.request.urlopen(url)
    return Path(req.url).name

def install(url: str, yes: bool = False) -> None:
    version = _version(url)
    url = f"{url}/releases/download/{version}/{Path(url).name}-{re.sub('[a-zA-Z]', '', version)}-py3-none-any.whl"
    yes = '-y' if yes else ''
    cmd = f'pip3 install --user --upgrade {yes} {url}'
    sp.run(cmd, shell=True, check=True)


def parse_args(args=None, namespace=None):
    """Parse command-line arguments for the install/configuration util.
    """
    parser = ArgumentParser(
        description='Automatically install the latest version of Python package from its GitHub project.'
    )
    parser.add_argument(
        '-y',
        '--yes',
        dest='yes',
        action='store_true',
        help='Yes to prompt questions.'
    )
    parser.add_argument(
        'url',
        help='The URL of the GitHub project of the Python package.'
    )
    return parser.parse_args(args=args, namespace=namespace)


def main():
    args = parse_args()
    install(args.url, args.yes)


if __name__ == '__main__':
    main()
