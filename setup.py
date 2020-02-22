import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='event-mocks-python',
    version='0.0.1',
    author='Abir Hossain',
    author_email='abir.hossain@sbs.com.au',
    description='A small Python library that includes details mocks of AWS Lambda event sources.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Abir-H/serverless-event-mocks-python',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
