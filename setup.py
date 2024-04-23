from setuptools import setup

setup(
        name='wordlist',
        version='1.1.0',
        install_requires=[
            ],
        entry_points={
            'console_scripts': [
                'wordlist=main:main',
                ],
            },
        py_modules=['main'],
        )
