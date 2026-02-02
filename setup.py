from setuptools import setup, find_packages

setup(
    name="frenchplotlib",
    version="0.4.0",
    description="French-themed matplotlib markers and colormaps",
    author="philzphaz",
    url="https://github.com/PhilZPhaZ/frenchplotlib",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "matplotlib",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={
        "frenchplotlib": ["assets/**/*"],
    },
)
