from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name="otfilesystemlibs",
  version="1.0.0",
  description='AWS Python Libraries',
  author='Rajat Vats',
  author_email='rajat.vats.opstree.com',
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=["otfilesystemlibs"],
  python_requires=">=3.6",
)