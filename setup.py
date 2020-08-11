from setuptools import setup

setup(name="djangohardening",
    version='1.0.0',
    description='Hardening system checks for Django',
    author='Joel Ryan',
    author_email='joel@iwcenter.com',
    packages=['hardening'],
    install_requires=["django>=2.2"],
    python_requires=">=3.5",
)
