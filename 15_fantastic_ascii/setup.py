from setuptools import setup, find_packages

fantastic_ascii_setup_args = dict(
    name='fantastic_ascii',
    version='2.0.0',
    description='Fantastic ASCII',
    license='MIT',
    install_requires=[
        'requests',
        'importlib-metadata; python_version == "3.8"',
        'boto3',
        'yt-dlp>=2023.2.17',
        'loguru'
        'pyTelegramBotAPI',
    ],
    author='Matt',
    author_email='example@example.com'
)

)

if __name__ == '__main__':
    setup(**fantastic_ascii_setup_args)

