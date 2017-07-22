from setuptools import setup

setup(
    name="ISSdata",
    version='0.1',
    py_modules=['issdata'],
    install_requires=[
        'Click',
        'tzlocal',
        'requests'
    ],
    entry_points='''
    [console_scripts]
    ISSdata=issdata:get_time
    '''
)
