from setuptools import setup, find_packages

setup(
    name='to-do-list',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SQLAlchemy',
    ],
    entry_points={
        'console_scripts': [
            'run=app:app.run'
        ],
    },
)
