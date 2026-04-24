import subprocess
from typing import Tuple, Optional


def _run(cmd: list[str]) -> Tuple[bool, str, str]:
	"""
	Interal helper to run an AWS CLI command. 
	Returns: (success, stdout, stderr)
	"""
	result = subprocess.run(cmd, capture_output=True, text=True)
	return result.returncode == 0, result.stdout, result.stderr

def aws_cp(
		src: str, 
		dst: str,
		profile: Optional[str] = None,
		region: Optional[str] = None
		) -> Tuple[bool, str, str]:

	"""
	Copy a file or prefix using 'aws s3 cp'
	"""

	cmd = ["aws","s3","cp", src, dst, "--only-show-errors"]
	
	if profile:
		cmd += ["--profile", profile]
	if region:
		cmd += ["--region", region]

	return _run(cmd)

def aws_ls(
		uri: str,
		profile: Optional[str] = None,
		region: Optional[str = None
		} -> Tuple[bool, str, str]:

		"""
		List S3 objects using 'aws s3 ls'
		"""

		cmd = ["aws", "s3", "ls", uri]

		if profile:
			cmd += ["--profile", profile]
		if region:
			cmd += ["--region", region]

		return _run(cmd)


