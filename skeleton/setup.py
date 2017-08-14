try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Andrew Freeman',
    'url': 'wheretofindit.com',
    'download_url': 'wheretodownloadit.org',
    'author_email': 'afreeman@simplereach.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'issa project'
}

setup(**config)
