
"""
Small helpers for path classification and S3 parsing
"""
from urllib.parse import urlparse

def is_s3_path(path: str) -> bool:
	"""
	Return True if the string looks like an S3 URI
	"""
	return path.startswith("s3://")

def is_local_path(path: str) -> bool:
	"""
	Return True if the path is not an S3 URI
	"""
	return not is_s3_path(path)

def split_s3_path(path: str):

	"""
	Split an S3 URI into (bucket, key)
	Example:
		s3://my-bucket/data/file.csv
		-> ("my-bucket", "data/file.csv")
	"""
	if not is_s3_path(path):
		raise ValueError(f"Not an S3 path: {path}")

	parsed = urlparse(path)
	bucket = parsed.netloc
	key = parsed.path.lstrip("/")
	
	return bucket, key
