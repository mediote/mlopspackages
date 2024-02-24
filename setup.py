from setuptools import find_packages, setup
from setuptools_scm import get_version

DESCRIPTION = 'Pacotes MLOPS reutilizáveis.'
LONG_DESCRIPTION = 'Pacotes MLOPS reutilizáveis.'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'

setup(
    name="mlopspackages",
    version=get_version(),
    author="Andre Mediote de Sousa",
    author_email="mediote90@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    packages=find_packages(exclude=("tests*", "docs")),
    setup_requires=['setuptools_scm'],
    install_requires=[
        'boto3',
        'pandas',
        'requests',
    ],
    keywords=['python', 'mlops', 'reusable packages'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        "Bug Tracker": "https://github.com/mediote/mlopspackages/issues",
        "Documentation": "https://github.com/mediote/mlopspackages#readme",
        "Source Code": "https://github.com/mediote/mlopspackages",
    },
)
