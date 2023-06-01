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
    ],
    author='Matt',
    author_email='example@example.com'
)

logger_package_setup_args = dict(
    name='logger',
    version='1.0.0',
    description='Loguru Package',
    license='MIT',
    install_requires=[
        'pip',
    ],
    author='Matt',
    author_email='example@example.com'
)

pytelegrambotapi_package_setup_args = dict(
    name='pytelegrambotapi_package',
    version='1.0.0',
    description='pyTelegramBotAPI Package',
    license='MIT',
    install_requires=[
        'pyTelegramBotAPI',
    ],
    author='Matt',
    author_email='example@example.com'
)

if __name__ == '__main__':
    setup(**fantastic_ascii_setup_args)
    setup(**boto3_package_setup_args)
    setup(**yt_dlp_package_setup_args)
    setup(**loguru_package_setup_args)
    setup(**pytelegrambotapi_package_setup_args)
