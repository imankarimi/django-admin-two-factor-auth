import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-admin-two-factor',
    version='0.0.1',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    description='Django Admin Two Factor Authentication',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/imankarimi/django-admin-two-factor-auth',
    author='Iman Karimi',
    author_email='imankarimi.mail@gmail.com',
    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Environment :: Web Environment',
        'Topic :: Software Development',
    ],
    install_requires=[
        'Django',
        'pyotp',
        'qrcode',
        'Pillow',
    ],
)
