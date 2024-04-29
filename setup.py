from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list[str]:
    '''
    This function reads the requirements.txt file and returns the list of requirements
    '''
    HYPEN_E_DOT = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Parimal',
    author_email="parimalnathreddy@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
