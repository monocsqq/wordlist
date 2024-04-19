from setuptools import setup

setup(
        name='wordlist',
        version='1.0.0',
        install_requires=[
            'pandas',
            ],
        entry_points={
            'console_scripts': [
                'wordlist=main:main',
                ],
            },
