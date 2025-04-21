from setuptools import setup, find_packages

setup(
    name="turkish_number_converter",
    version="0.1",
    description="Türkçe yazıyla yazılmış sayıları rakama çeviren Python modülü",
    author="Arif ACAY",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
