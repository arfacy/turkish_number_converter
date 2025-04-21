from setuptools import setup

setup(
    name="turkish_number_converter",
    version="0.1",
    description="Türkçe yazıyla yazılmış sayıları rakama çeviren Python modülü",
    author="Arif ACAY",
    packages=["turkce_sayi"],  # 📌 bu klasörün adı
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
