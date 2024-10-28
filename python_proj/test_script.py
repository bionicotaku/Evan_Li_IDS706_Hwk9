import unittest
import io
from contextlib import redirect_stdout
import os
from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        # check if the dataset file exists
        dataset_path = "../data/Dataset-salary-2024.csv"
        self.assertTrue(
            os.path.exists(dataset_path), f"Dataset file {dataset_path} does not exist."
        )

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            main()
        output = captured_output.getvalue()

        self.assertTrue(output)


if __name__ == "__main__":
    unittest.main()
