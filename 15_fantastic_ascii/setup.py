from setuptools import setup, find_packages


yt_dlp_package_setup_args = dict(
    name='yt_dlp_package',
    version='2023.2.17',
    description='yt-dlp Package',
    license='MIT',
    install_requires=[
        'yt-dlp>=2023.2.17',
    ],
    author='Matt',
    author_email='example@example.com'
)



if __name__ == '__main__':

    setup(**yt_dlp_package_setup_args)


