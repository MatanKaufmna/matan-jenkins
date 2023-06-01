from setuptools import setup, find_packages

setup_args = [
    {
        'name': 'fantastic_ascii',
        'version': '2.0.0',
        'description': 'Fantastic ASCII',
        'license': 'MIT',
        'install_requires': [
            'requests',
            'importlib-metadata; python_version == "3.8"',
        ],
        'author': 'Matt',
        'author_email': 'example@example.com'
    },
    {
        'name': 'boto3_package',
        'version': '1.0.0',
        'description': 'Boto3 Package',
        'license': 'MIT',
        'install_requires': [
            'boto3',
        ],
        'author': 'Matt',
        'author_email': 'example@example.com'
    },
    {
        'name': 'yt_dlp_package',
        'version': '1.0.0',
        'description': 'yt-dlp Package',
        'license': 'MIT',
        'install_requires': [
            'yt-dlp>=2023.2.17',
            'pyTelegramBotAPI',
        ],
        'author': 'Matt',
        'author_email': 'example@example.com'
    },
    {
        'name': 'loguru_package',
        'version': '1.0.0',
        'description': 'Loguru Package',
        'license': 'MIT',
        'install_requires': [
            'loguru',
        ],
        'author': 'Matt',
        'author_email': 'example@example.com'
    }
]

if __name__ == '__main__':
    for setup_arg in setup_args:
        setup(**setup_arg)
