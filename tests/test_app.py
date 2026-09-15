import tempfile
import unittest
from pathlib import Path

from app import check_repository


class TestRepositoryHealth(unittest.TestCase):
    def test_complete_repository(self):
        with tempfile.TemporaryDirectory() as folder:
            repository = Path(folder)
            (repository / "README.md").touch()
            (repository / "tests").mkdir()
            (repository / "requirements.txt").touch()

            result = check_repository(repository)

            self.assertTrue(all(result.values()))

    def test_incomplete_repository(self):
        with tempfile.TemporaryDirectory() as folder:
            result = check_repository(Path(folder))

            self.assertFalse(result["README.md"])
            self.assertFalse(result["tests folder"])
            self.assertFalse(result["requirements.txt"])


if __name__ == "__main__":
    unittest.main()
