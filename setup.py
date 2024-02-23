from setuptools import find_packages, setup

VERSION = '0.0.1'
DESCRIPTION = 'Meu primeiro pacote em Python'
LONG_DESCRIPTION = 'Meu primeiro pacote em Python com uma descrição um pouco mais longa'

requires = [
    'boto3',
    'pandas',
    'requests',
]

# Setting up
setup(
    name="mlopspackages",
    version=VERSION,
    author="Andre Mediote de Sousa ",
    author_email="mediote90@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=requires,
    dependency_links=[
        'https://github.com/mediote/mlopspackages.git#egg=search',
        'https://github.com/mediote/mlopspackages.git#egg=solr',
    ],
    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix :: Ubuntu",
        "Operating System :: Microsoft :: Windows",
    ]
)
