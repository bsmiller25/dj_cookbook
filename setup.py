from setuptools import setup, find_packages

setup(name='dj_cookbook',
      version='0.1',
      description='Simple cookbook app',
      url='',
      author='Ben Miller',
      author_email='bsmiller25@gmail.com',
      license='',
      packages=find_packages(),
      install_requires=[
          'requests',
          'django',
      ],
      include_package_data=True,
      zip_safe=False)
