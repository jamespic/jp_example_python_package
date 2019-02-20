from setuptools import setup, find_packages
from setuptools.extension import Extension

with open('README.md') as f:
    readme = f.read()

setup(
    name='jp-example-python-package',
    version='1.0.0',
    author='James Pickering',
    author_email='james.pickering@airelogic.com',
    description="An example of a Python package",
    long_description=readme,
    long_description_content_type='text/markdown',
    url="https://github.com/jamespic/example_python_package",
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    ext_modules=[
        Extension('jp_example_python_package.native',
                  ['src/jp_example_python_package/native.pyx'])
    ],
    python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
