import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrpgkit",
    version="0.0.1",
    author="feakuru",
    author_email="feanarokurufinve@gmail.com",
    description="A library for writing RPGs in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feakuru/pyrpgkit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)