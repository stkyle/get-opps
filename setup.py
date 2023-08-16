
from setuptools import setup, find_packages

setup(
    name='OpportunitiesAPIClient',
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'httpx',
        'ratelimit',
        'tenacity',
        'cachetools',
        'pydantic',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python client for the Opportunities API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/OpportunitiesAPIClient',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
