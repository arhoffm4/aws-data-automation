"""
Command-line interface fo datamove
"""
import argparse
import sys
from pathlib import Path

from .mover import DataMover
from .checksum import sha256sum
from .utils import is_local_path


def build_parser() -> argparse.ArgumentParser:


	parser = argparse.ArgumentParser(
			prog="datamove",
			description="Data movement with checksum verification"
			)

	sub = parser.add_subparsers(dest="command", required=True)

	"""
	-----------------
	datamove SRC DST
	-----------------
	"""
	verify = sub.add_parser("verify", help="Compute SHA-256 cehcksum of a local file")
	verify.add_argument("path", help="Local file path")

	return parser

def main(argv=None) -> int:
	parser = build_parser()
	args = parser.parse_args(argv)

	if args.command == "move":
		mover = DataMover()
		ok = mover.move(args.src, args.dst)
		return 0 if ok else 1

	if args.command == "verify":
		path = Path(args.path)
		if not is_local_path(args.path):
			print("Verify only works on local files", file=sys.stderr)
			return 1

		if not path.exists():
			print(f"file not found: {path}", file=sys.stderr)
			return 1

		checksum = sha256sum(path)
		print(f"SHA-256: {checksum}")
		return 0

	# Should never reach here
	parser.print_help()
	return 1

if __name__ == "__main__":
	sys.exit(main())



using argparse:
datamove move localfile.txt s3://bucket/path/
datamove move s3://bucket/file localfile.txt
datamove verify localfile.txt
