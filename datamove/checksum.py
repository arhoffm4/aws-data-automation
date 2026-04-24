"""
minimal SHA-256 checksum helper for datamove
"""

import hashlib
from pathlib import Path

def sha256sum(path: str | Path, block_size=65536) -> str:
	"""
	Compute the SHA-256 checksum of a file

	Args:
		path: File path (string or Path object)
		block_size: How many bytes to read at a time

	Returns:
		Hex-encoded SHA-256 digest
	"""
	path = Path(path)
	h = hashlib.sha256()
	with path.open("rb") as f:
		for chunk in iter(lambda: f.read(block_size), b""):
			h.update(chunk)
	
	return h.hexdigest()
