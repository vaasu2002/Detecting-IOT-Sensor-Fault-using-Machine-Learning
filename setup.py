from setuptools import find_packages, setup

PROJECT_NAME="Kafka Producer Consumer Script for Sensor Data"
VERSION="0.0.2"
AUTHOR="Vaasu Bisht"
DESRCIPTION="In this project I will be bulding a pipeline to train and test a machine learning model, I will try to use the format which is used in industry."

REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name=PROJECT_NAME.
    version=VERSION,
    author=AUTHOR,
    description = DESRCIPTION,
    author_email="bishtvaasu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements_list()
)
