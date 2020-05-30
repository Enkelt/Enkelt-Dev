import setuptools

long_description = '''
'''

setuptools.setup(
    name="Enkelt",
    version="4.1",
    author="Edvard Busck-Nielsen",
    author_email="me@edvard.io",
    description="Enkelt is the world's first Swedish programming language, and the perfect choice for programming education in swedish.",
    long_description="Enkelt is the world's first Swedish programming language, and the perfect choice for programming education in swedish.",
    url="https://enkelt.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Natural Language :: Swedish",
    ],
    python_requires='>=3.6',
)
