from setuptools import setup

setup(
    name='cli',
    version='1.0',
    py_modules=['hello','bam'],
    install_requires=[
      'click',
    ],
    entry_points='''
      [console_scripts]
      hello=hello:cli
      bam=bam:cli
    ''',
)
