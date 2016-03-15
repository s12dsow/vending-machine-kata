try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Vending Machine',
    'author': 'Dicko Sow',
    'url': '',
    'download_url': '',
    'author_email': '',
    'version': '0.1',
    'install_requires': ['unittest'],
    'packages': ['vending_machine'],
    'scripts': [],
    'name': 'Vending Machine'
}

setup(**config)
