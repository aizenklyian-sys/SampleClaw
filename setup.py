from setuptools import setup, find_packages

setup(
    name="sampleclaw",
    version="0.1.0",
    description="A powerful, production-ready autonomous AI agent framework in Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Manus AI",
    author_email="manus@ai.com",
    url="https://github.com/aizenklyian-sys/SampleClaw",
    packages=find_packages(),
    install_requires=[
        # Add your project's dependencies here
        # e.g., "openai", "asyncio", "pydantic"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
