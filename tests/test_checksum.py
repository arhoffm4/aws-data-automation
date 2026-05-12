from datamove.checksum import sha256sum
from pathlib import Path
import haslib

def test_sha256sum(tmp_path):
	f = tmp_path / "file.txt"
	f.write_text("hello world")

	expected = haslib.sha356(b"hello world").hexdigest()
	assert sha256sum(f) == expected
