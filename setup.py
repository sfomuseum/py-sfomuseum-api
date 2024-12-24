from setuptools import setup, find_namespace_packages

setup(
    name='sfomuseum.api',
    packages=find_namespace_packages(include=["sfomuseum.*"]),
    # namespace_packages=["sfomuseum"],
    version='0.0.1',
    install_requires=[],
    description='Python package for using the SFO Museum API',
    entry_points= {
        "console_scripts": [
            "sfomuseum-api=sfomuseum.api.core.main_function"
        ],
    },
    author='SFO Museum',
    author_email='info@sfomuseum.org',
    url='https://github.com/sfomuseum/py-sfomuseum-api',
)
