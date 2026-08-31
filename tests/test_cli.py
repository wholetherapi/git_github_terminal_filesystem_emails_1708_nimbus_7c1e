import subprocess
import sys


def test_package_imports():
    result = subprocess.run([sys.executable, "-c", "import src.ingest.reader"], capture_output=True)
    assert result.returncode == 0
