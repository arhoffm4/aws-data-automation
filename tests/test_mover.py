from datamove.mover import DataMover
import subprocess
import shutil

def test_local_to_local(tmp_path, monkepatch):
	src = tmp_path / "src.txt"
	dst = tmp_path / "dst.txt"
	src.write_text("hello")

	mover = DataMover()

	ok = mover.move(str(src), str(dst))
	assert ok
	assert dst.read_text() == "hello"
