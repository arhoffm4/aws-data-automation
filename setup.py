from setuptools import setup, find_packages

setup(
		name="datamove",
		version="0.1.0",
		description="Minimal data movement tool with AWS CLI integration and checksum verification",
		author="Andrew Hoffman",
		packages=find_packages(),
		python_requires=">=3.8",
		install_requires=[],
		entry_points={
			"console_scripts": [
				"datamove=datamove.cli:main",
			],
		},
	 )
