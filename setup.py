# Always prefer setuptools over distutils
import re
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get current version
with open(path.join(here, 'ctr_core', '__init__.py')) as fp:
    main_package = fp.read()
version_re = r"^__version__\s*=\s*['\"]([^'\"]*)['\"]"
version_match = re.search(version_re, main_package, re.M)
if not version_match:
    raise RuntimeError("Unable to find version string.")
__version__ = version_match.group(1)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ctr-core',
    version=__version__,
    description='Core Python library for Avblox services',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CodeToRelax/ctr-backend-core',
    author='CTR',
    author_email='mustafa@ctr.ly',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='aws lambda api gateway',
    packages=find_packages(),
    python_requires='>=3.7',
)
