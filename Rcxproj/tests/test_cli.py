import unittest
from subprocess import run

class TestCLI(unittest.TestCase):
    def test_build_command(self):
        result = run(["python3", "rcxproj/cli.py", "build", "--file", "project.rcxproj"])
        self.assertEqual(result.returncode, 0)

if __name__ == '__main__':
    unittest.main()