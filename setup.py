from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    install_requires=[
        'Django',
        'pyotp',
        'qrcode',
        'Pillow',
    ],
    include_package_data=True,
    zip_safe=False
)