from dataclasses import dataclass
from typing import Optional

from .logger import get_logger
from .checksum import sha256sum
from .aws import aws_cp
from .utils import is_local_path, is_s3_path

@dataclass
class DataMover:
	"""
	Simple orchestrator for moving data between local paths and S3.

	Demonstrates:
		- logging
		- retries
		- checksum verification
		- AWS CLI integration
	"""

	retries: int = 3
	logger_name: str = "datamove"
	

	def __post_init__(self):
		self.logeer = get_logger(self.logger_name)

	def move(self, src: str, dst: str) -> bool:
		self.logger.info(f"Starting transfer: {src} -> {dst}")
		
		# Pre-transfer checksum (local only)
		src_checksum: Optional[str] = None
		if is_local_path(src):
			self.logger.info(f"Computing checksum for source: {src}")
			src_checksum = sha256sum(src)

		# Transfer with retries
		if not self._transfer_with_retries(src, dst):
			self.logger.error("Transfer failed after retries")
			return False
			
		# Post-transfer checksum (local only)
		if is_local_path(dst) and src_checksum:
			self.logger.info(f"Computing checksum for destination: {dst}")
			dst_checksum = sha256sum(dst)
			if dst_checksum != src_checksum:
				self.logger.error("Checksum mismatch between source and destination")
				return False

		self.logger.info("Transfer complete and verified")
		return True

	def _transfer_with_retries(self, src: str, dst: str) -> bool:
		"""
		Retry wrapper for the transfer operation
		"""
		for attempt in range(1, self.retries + 1):
			self.logger.info(f"Transfer attempt {attempt}/{self.retries}")
			ok, out, err = self._transfer_once(src, dst)
			if ok:
				if out:
					self.logger.info(out.strip())
				return True
			self.logger.warning(f"Transfer {attempt} failed: {err.strip()}")
		return False

	def _transfer_once(sef, src: str, dst: str):
		# local -> S3 
		if is_local_path(src) and is_s3_path(dst):
			return aws_cp(src, dst)

		# S3 -> local
		if is_s3_path(src) and is_local_path(dst):
			return aws_cp(src, dst)

		# local -> local placeholder
		self.logger.error("Local -> local tranfer not implemented yet")
		return False, "", "local-local not implemented"
					
