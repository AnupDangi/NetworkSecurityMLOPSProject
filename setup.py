'''
The setup.py file is an essential part of a Python project that is used for packaging and distributing the project. 
It is used by setuptools, a popular library for packaging Python projects. The setup.py file contains metadata about the project,
such as its name, version, author, and dependencies. It also defines how the project should be built and installed.
'''


from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str)-> List[str]:
    """Reads the requirements from a file and returns them as a list of strings."""
    try:
        requirements_lst :List[str]=[]
        with open(file_path,'r') as file:
            lines= file.readlines()
            for line in lines:
                requirements_lst =line.strip()
                
                if line and line!='-e .':
                    requirements_lst.append(line)
    except Exception as e:
        print(f"Error reading requirements file: {e}")

    return requirements_lst


setup(
    name="NetworkSecurityMLOPSProject",
    version="0.1.0",
    author="Anup Dangi",
    author_email="anupdangi1589@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description="A project for Network Security using MLOps practices.",
)





