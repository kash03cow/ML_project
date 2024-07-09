from setuptools import find_packages,setup
from typing import List

def get_requirements(package_name:str)->List[str]:
    '''
    this functions returns the list of requirements
    '''
    requirements=[]
    with open(package_name) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if("-e .") in requirements:
            requirements.remove("-e .")
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Keshav',
author_email='keshavkb3@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)