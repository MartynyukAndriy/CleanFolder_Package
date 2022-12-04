from setuptools import setup, find_namespace_packages


setup(
    name="Clean Folders",
    version="0.0.1",
    description="Cleaning folders",
    author="Andriy Martynyuk",
    author_email="andriy.martynyuk.if@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    packages=find_namespace_packages(),
    include_package_data=True,
    data_files=[("clean_folder", ["clean_folder/translate.py"])],
    entry_points={"console_scripts": [
        "cleanfolder=clean_folder.sort:clean"]}
)
