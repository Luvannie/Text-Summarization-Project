import setuptools
with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarization-Project"
AUTHOR_USER_NAME = "Luvannie"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "nhatanh.2552002@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="a project about Text Summarization  i learn from Youtube",
    long_description= long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/Luvannie/Text-Summarization-Project",
    project_urls= {
        "Bug tracker": f"https://github.com/Luvannie/Text-Summarization-Project/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)