import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NKSC", # Replace with your own username
    version="0.0.1",
    author="Sarah Dandou",
    author_email="dandousarah@gmail.com", 
    description="a KShell computing package for networkx graph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cgonzalez-gomez/networkx-KShell-computing.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

print(setuptools.find_packages())