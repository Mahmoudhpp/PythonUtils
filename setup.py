from setuptools import setup, find_packages

VERSION = '0.1.9'
DESCRIPTION = 'IceCreamSwap Python utility package'
LONG_DESCRIPTION = 'IceCreamSwap Python utility package'

requirements = [
    'pandas',
    'numpy',
    'web3',
    'pyarrow',
    'redis',
    'requests'
]

# Setting up
setup(
    name="icecreamswaputils",
    version=VERSION,
    author="IceCreamSwap",
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=requirements,
    # needs to be installed along with your package.

    keywords=['python', 'icecreamswaputils'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
