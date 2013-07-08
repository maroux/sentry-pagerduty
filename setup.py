#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.3.3'
    'git+git://github.com/depop/pygerduty.git'
]

f = open('README.md')
readme = f.read()
f.close()

setup(
    name='sentry-pagerduty',
    version='0.0.1',
    author='Leonid Berov',
    author_email='leon@depop.com',
    url='https://github.com/depop/sentry-pagerduty',
    description='A Sentry plugin for sending error occurences to a Pagerduty instance.',
    long_description=readme,
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'sentry.plugins': [
            'sentry_pagerduty = sentry_pagerduty.plugin:PagerdutyPlugin'
        ],
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development'
    ],
    keywords='sentry pagerduty',
)
