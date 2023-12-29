import setuptools
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_reqs = [x.strip() for x in all_reqs if 'git+' not in x]
dep_links = [x.strip().replace('git+', '') for x in all_reqs if 'git+' in x]

with open(path.join(here, 'readme.org'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="dmpc_security",
    version="0.0.0",
    author='Rafael Accácio',
    author_email='rafael.accacio.nogueira',
    url='https://github.com/Accacio/dmpc_security',
    description="Tests with distributed Model Predictive Control under attack",
    long_description=long_description,
    long_description_content_type='text/plain',
    packages=setuptools.find_packages(where='src', exclude=['env', 'tests', 'infrastructure']),
    include_package_data=True,
    install_requires=install_reqs,
    package_dir={'': 'src'},
    dependency_links=dep_links)
