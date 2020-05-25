import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="facebookapi", # Replace with your own username
    version="0.0.3",
    author="Xavier",
    author_email="collantes.xavier@gmail.com",
    description="Facebook API handler.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xcollantes/facebook-api",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests",
        "pyyaml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
