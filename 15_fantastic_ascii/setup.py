from setuptools import setup, find_packages



boto3_package_setup_args = dict(
    name='boto3_package',
    version='1.0.0',
    description='Boto3 Package',
    license='MIT',
    install_requires=[
        'boto3',
    ],
    author='Matt',
    author_email='example@example.com'
)



if __name__ == '__main__':
    setup(**boto3_package_setup_args)

