from setuptools import setup

setup(
        name='wordlist',
        version='1.1.1',
        install_requires=[
            'googletrans==4.0.0-rc1',
            'timeout-decorator==0.5.0',
            ],
        entry_points={
            'console_scripts': [
                'wordlist=main:main',
                ],
            },
        py_modules=['main'],
        )
