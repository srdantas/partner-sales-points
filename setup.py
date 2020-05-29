import setuptools

setuptools.setup(
    name='partners',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'cerberus',
        'werkzeug',
        'pymongo'
    ],
    extras_require={"tests": ['pytest',
                              'coverage',
                              'testcontainers']}
)
