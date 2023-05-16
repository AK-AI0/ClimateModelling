from setuptools import find_packages,setup
from typing import List # To use while defining a function and mention that it returns a list

hyphen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    the function specifies a list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
name = "ClimateModelling",
version = "0.0.1",
author="ak",
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)