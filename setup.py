from setuptools import setup

setup(
    name="FPick",
    version="0.1",
    description="Open the file dialog from CLI",
    author="coding-beagle",
    author_email="nicholasp.teague@gmail.com",
    packages=["fpick"],
    install_requires=["Click"],
    extras_require={
        "dev": ["pytest", "pytest-cov", "wheel", "pyinstaller", "build"],
        "test": ["pytest", "pytest-cov"],
    },
    entry_points="""
        [console_scripts]
        fpick=fpick.__main__:cli
    """,
)
