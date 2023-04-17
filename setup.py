from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    """This function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        # This reads the line from the file one by one
        # During reading the new line words adds '\n'; so we need to remove this, otherwise it may cause any error
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', "") for req in requirements]

        if  HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'PRASANNA',
    author_email = 'harkep20@outlook.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)
