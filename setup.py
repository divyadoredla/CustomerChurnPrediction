"""
Setup script for Customer Churn Prediction package
"""
from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    Read requirements from file
    
    Args:
        file_path: Path to requirements.txt
        
    Returns:
        List of requirement strings
    """
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='customer_churn_prediction',
    version='1.0.0',
    author='Divya Sri Doredla',
    author_email='divyasri@example.com',
    description='Production-ready Customer Churn Prediction System',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/divyasridoredla/customer-churn-prediction',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8',
    keywords='machine-learning churn-prediction customer-analytics ml-pipeline',
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/customer-churn-prediction/issues',
        'Source': 'https://github.com/yourusername/customer-churn-prediction',
    },
)
