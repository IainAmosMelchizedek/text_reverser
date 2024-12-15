from setuptools import setup

setup(
    name="text_reverser",
    version="0.1.0",
    py_modules=["reverse_text"],
    entry_points={
        "console_scripts": [
            "text-reverser=reverse_text:main",
        ],
    },
    author="Iain Amos Melchizedek",
    author_email="iainamos@outlook.com",
    description="A simple tool to reverse text.",
    long_description="This package provides a simple command-line tool to reverse input text. "
                     "It is built for educational purposes to demonstrate packaging with Conda.",
    long_description_content_type="text/plain",
    license="MIT",
    url="https://github.com/IainAmosMelchizedek/text_reverser",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

