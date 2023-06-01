from setuptools import setup, find_packages

fantastic_ascii_setup_args = dict(
    name='fantastic_ascii',
    version='2.0.0',
    description='Fantastic ASCII',
    license='MIT',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
    ],
    author='Matt',
    author_email='example@example.com'
)

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

yt_dlp_package_setup_args = dict(
    name='yt_dlp_package',
    version='1.0.0',
    description='yt-dlp Package',
    license='MIT',
    install_requires=[
        'yt-dlp>=2023.2.17',
        'pyTelegramBotAPI',
    ],
    author='Matt',
    author_email='example@example.com'
)

loguru_package_setup_args = dict(
    name='loguru_package',
    version='1.0.0',
    description='Loguru Package',
    license='MIT',
    install_requires=[
        'loguru',
    ],
    author='Matt',
    author_email='example@example.com'
)



setup(**fantastic_ascii_setup_args)
setup(**boto3_package_setup_args)
setup(**yt_dlp_package_setup_args)
setup(**loguru_package_setup_args)

