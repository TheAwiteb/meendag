from setuptools import setup, find_packages
import re

KEYWORD = ["meendag", "Meendag", "number-owner"]

with open("meendag/__init__.py", "r", encoding="utf-8") as f:
    version = re.search(
        r'^version\s*=\s*"(.*)".*$', f.read(), flags=re.MULTILINE
    ).group(1)

with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt", encoding="utf-8") as require_file:
    requires = [require.strip() for require in require_file]

setup(
    name="meendag",
    version=version,
    description="An unofficial SDK for Meendag.com help you to find name of the owner of the number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Awiteb",
    author_email="Awiteb@hotmail.com",
    url="https://github.com/TheAwiteb/meendag",
    packages=find_packages(),
    license="AGPL",
    keywords=KEYWORD,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requires,
)
