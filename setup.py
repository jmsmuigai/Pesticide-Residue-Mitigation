from setuptools import setup, find_packages

setup(
    name="safeplate-platform",
    version="6.0.0",
    description="SafePlate Kenya v6 — Pesticide Residue Mitigation, MAKTABA Library & MSAIDIZI Assistant Engine",
    author="SafePlate Team",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn>=0.20.0",
        "pydantic>=1.10.0",
    ],
    entry_points={
        "console_scripts": [
            "safeplate-assistant=safeplate_platform.assistant:run_cli",
        ],
    },
)
