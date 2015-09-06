from setuptools import setup, find_packages

setup(
    name='emcee_functools',
    author='Simon Walker',
    author_email='s.r.walker101@googlemail.com',
    install_requires=[
        'emcee',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)

