from setuptools import find_packages, setup

setup(
    name='email_service',
    description='email_service',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    test_suite="tests",
    zip_safe=False)
