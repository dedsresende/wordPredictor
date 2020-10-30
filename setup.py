from setuptools import setup

setup(
    name='wordPredictor',
    version='0.0.1',
    description='Rank words based on their similarity',
    url='git@gitlab.com:dedsresende/tm_dash.git',
    author='Andre Resende',
    author_email='dedsresende@gmail.com',
    license='unlicense',
    packages=['tm_dash'],
    zip_safe=False,
    install_requires=[
       'pandas >= 0.24.2',
       'Shapely >= 1.6.4.post2',
       'numpy >= 1.13.3',
       'colormap >= 1.0.3',
       'matplotlib >= 3.2.2',
       'plotly >= 4.8.2',
       'scipy >= 1.5.1'
    ]
)