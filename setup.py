from setuptools import find_packages, setup


def readfile(filename):
    with open(filename, "r+") as f:
        return f.read()


setup(
    name="codesage",
    version="0.1.8",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "codesage": ["sample-exclude.txt"],
    },
    install_requires=open("requirements.txt").readlines() + ["setuptools"],
    entry_points={
        "console_scripts": [
            "r2v-index=codesage.index:main",
            "r2v-chat=codesage.chat:main",
        ],
    },
    author="Julia Turc & Mihail Eric / Storia AI",
    author_email="founders@storia.ai",
    description="A library to index a code repository and chat with it via LLMs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Storia-AI/codesage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
