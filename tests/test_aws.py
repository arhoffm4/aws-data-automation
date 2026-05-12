from datamove.aws import aws_cp
import subprocess

def test_aws_cp(monkeypatch):
	def fake_run(cmd, capture_output, text):
		class R:
			returncode = 0
			stdout = "ok"
			stderr = ""
		return R()

	monkeypatch.setattr(subprocess, "run", fake_run)

	ok, out, err = aws_cp("a", "b")
	assert ok
	assert out == "ok"
