from setuptools import setup

setup(
    name='gophish',
    packages=['gophish', 'gophish.api'],
    version='0.2.5',
    description='Python API Client for Gophish',
    author='Jordan Wright',
    author_email='python@getgophish.com',
    url='https://github.com/gophish/api-client-python',
    license='MIT',
    download_url='https://github.com/gophish/api-client-python/tarball/0.2.2',
    keywords=['gophish'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
