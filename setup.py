import versioneer
from os import path
from setuptools import setup, find_packages
import sys

min_version = (3, 6)

if sys.version_info < min_version:
    error = """
qtpyinheritance does not support Python {0}.{1}.
Python {2}.{3} and above is required. Check your Python version like so:

python3 --version

This may be due to an out-of-date pip. Make sure you have pip >= 9.0.1.
Upgrade pip like so:

pip install --upgrade pip
""".format(*sys.version_info[:2], *min_version)
    sys.exit(error)


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(path.join(here, 'requirements.txt')) as requirements_file:
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]


setup(
    name='qtpyinheritance',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    license='BSD',
    author='Ken Lauer',
    packages=find_packages(exclude=['docs', 'tests']),
    description='Prototype qtpy inheritance-related tools',
    long_description=readme,
    url='https://github.com/klauer/qtpyinheritance',
    include_package_data=True,
    package_data={
        'qtpyinheritance': [
            ]
        },
    install_requires=requirements,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
)
