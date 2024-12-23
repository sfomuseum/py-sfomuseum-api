from setuptools import setup, find_packages

setup(
    name='sfomuseum.api',
    packages=find_namespace_packages(include=["sfomuseum.*"]),
    namespace_packages=["sfomuseum"],
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
    ],
    description='Python package for using the SFO Museum API',
    author='SFO Museum',
    author_email='info@sfomuseum.org',
    url='https://github.com/sfomuseum/py-sfomuseum-api',
)
