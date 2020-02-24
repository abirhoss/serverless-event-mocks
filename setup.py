import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='serverless-event-mocks',
    packages=['serverless_event_mocks'],
    version='0.0.7',
    license='MIT',
    description='A small Python library that includes details mocks of AWS Lambda event sources.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Abir Hossain',
    author_email='abirz.pro@gmail.com',
    url='https://github.com/abirhoss/serverless-event-mocks',
    download_url='https://github.com/abirhoss/serverless-event-mocks/archive/v0.0.7.tar.gz',
    keywords=['serverless', 'serverless-framework', 'unittest', 'mock', 'events', 'aws-lambda'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)
