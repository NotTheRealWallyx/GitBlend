from setuptools import setup, find_packages

setup(
    name="gitblend",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gitblend=gitblend.cli:main",
        ],
    },
    install_requires=[],
    author="Your Name",
    description="A Git utility tool combining git and gh commands",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
)
