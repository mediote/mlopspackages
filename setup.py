from setuptools import find_packages, setup

VERSION = '0.0.1'
DESCRIPTION = 'Meu primeiro pacote em Python'
LONG_DESCRIPTION = 'Meu primeiro pacote em Python com uma descrição um pouco mais longa'
LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'  # Altere conforme necessário

requires = [
    'boto3',
    'pandas',
    'requests',
]

setup(
    name="mlopspackages",
    version=VERSION,
    author="Andre Mediote de Sousa",
    author_email="mediote90@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    packages=find_packages(exclude=("tests*", "docs")),
    install_requires=requires,
    keywords=['python', 'first package'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",  # Modificado de Education para Developers
        "License :: OSI Approved :: MIT License",  # Exemplo, altere conforme sua licença
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",  # Se for verdade, é uma prática melhor do que especificar sistemas operacionais
    ],
    python_requires='>=3.6',  # Especifique a versão mínima do Python
    project_urls={  # URLs opcionais
        "Bug Tracker": "https://github.com/seuusuario/mlopspackages/issues",
        "Documentation": "https://github.com/seuusuario/mlopspackages#readme",
        "Source Code": "https://github.com/seuusuario/mlopspackages",
    },
)
