from setuptools import setup # importa o modulo setup

setup( # inicia a funçao setup
    name="notesCLI",
    version="0.1.0",
    py_modules=["notes"],
    entry_points={
        'console_scripts': [
            'nc=notes:main', # define o atalho para o script
        ],
    },
)