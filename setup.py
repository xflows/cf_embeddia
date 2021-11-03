from setuptools import setup, find_packages
import os

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
]

dist = setup(
    name='cf_embeddia',
    version='0.1',
    author='Vid Podpecan',
    description='Wrapper widgets for services developed in the EU Embeddia project.',
    url='https://github.com/xflows/cf_embeddia',
    license='MIT License',
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
)
