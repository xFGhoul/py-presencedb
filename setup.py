from distutils.core import setup

setup(
    name="presencedb",
    packages=["presencedb"],
    version="2.0.0",
    license="MIT",
    description="API wrapper for the presencedb (undocumented) api",
    author="Ghoul",
    url="https://github.com/xFGhoul/py-presencedb",
    keywords=["discord", "api", "presencedb", "discord-api", "discord bot"],
    install_requires=["aiohttp", "humanize"],
    extra_requires={"docs": ["mkdocs-material"], "tests": ["pytest"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
