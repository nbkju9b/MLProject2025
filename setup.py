#This file is used to insall my project as a package , even in PyPI

from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return a list of requirements from the given file path.
    :param file_path: str - path to the requirements file
    :return: list[str] - list of requirements
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
    name="MLProject2025",
    version="0.0.1",
    author="Arti Awasthi",
    author_email="arti.awasthi@gmail.com",
    description="A Machine Learning Project",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt"),
)