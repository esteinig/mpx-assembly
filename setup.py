from setuptools import setup, find_packages

setup(
    name="mpx-assembly",
    url="https://github.com/esteinig/mpx-assembly",
    author="Eike Steinig",
    author_email="eike.steinig@unimelb.edu.au",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer"
    ],
    entry_points="""
    [console_scripts]
    mpx=mpx.terminal:app
    """,
    version="0.1.0",
    license="MIT",
    description="Monkeypox assembly and all that other stuff",
)