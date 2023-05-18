from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .' #To trigger setup.py automatically
def get_requirements(filepath:str)->List[str]:
    '''
    This function will get required packages from requirements.txt
    '''
    requirements = []
    with open(filepath) as f:
        requirements = f.readlines()
        requirements= [req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="ML_with_AWS_deployment",
    version='0.0.1',
    author='Vijay Thamalla',
    author_email='vijayvthamalla@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)