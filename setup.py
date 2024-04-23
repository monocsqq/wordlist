from setuptools import setup

setup(
        name='wordlist',
        version='1.0.1',
        install_requires=[
            ],
        entry_points={
            'console_scripts': [
                'wordlist=main:main',
                ],
            },
        py_modules=['main'],
        )
