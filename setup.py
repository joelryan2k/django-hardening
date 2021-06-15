from setuptools import setup

setup(name="django-hardening",
    version='1.0.0',
    description='Hardening system checks for Django',
    author='Joel Ryan',
    author_email='joel@iwcenter.com',
    packages=['hardening'],
    install_requires=[
        "django>=2.2",
        "django-axes==5.4.3",
        "django-csp==3.6"
    ],
    python_requires=">=3.5",
)
