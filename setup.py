from setuptools import setup

setup(
    name='wordPredictor',
    version='0.0.1',
    description='Rank words based on their similarity',
    url='git@github.com:dedsresende/wordPredictor.git',
    author='Andre Resende',
    author_email='dedsresende@gmail.com',
    license='unlicense',
    packages=['tm_dash'],
    zip_safe=False,
    install_requires=[
        'Unidecode >= 1.1.1',
        'scikit_learn >= 0.23.2'
    ]
)