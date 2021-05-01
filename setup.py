from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


setup(
    name='imWatermark',
    version='0.0.2',
    author="mamdasn s",
    author_email="<mamdassn@gmail.com>",
    url="https://github.com/Mamdasn/imWatermark",
    description='This snippet of code attempts to watermark images.',
    long_description=long_description,
    long_description_content_type = "text/markdown",
    include_package_data=True,
    package_dir={'': 'src'},
    py_modules=["imWatermark"],
    install_requires=[
        "numpy", 
        "imhist",
        ],
    keywords=['python', 'histogram', 'Watermark', 'Watermark Image'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ]
)
