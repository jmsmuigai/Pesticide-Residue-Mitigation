from setuptools import setup, find_packages

setup(
    name="safeplate_platform",
    version="2.0.0",
    description="SafePlate Kenya v2 - AI-Driven Pesticide Residue Mitigation & Organic Alternatives Platform",
    author="SafePlate Engineering Team",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.95.0",
        "uvicorn>=0.20.0",
        "pydantic>=1.10.0",
        "requests>=2.28.0",
        "streamlit>=1.20.0",
        "folium>=0.14.0",
        "streamlit-folium>=0.11.0",
        "python-dotenv>=1.0.0"
    ],
    entry_points={
        "console_scripts": [
            "safeplate-agent=safeplate_platform.gemini_agent:run_gemini_tasks",
            "safeplate-test=safeplate_platform.hydrology:self_test"
        ],
    },
    python_requires=">=3.8",
)
