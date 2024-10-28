import unittest
import os
from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        # Check if the dataset file exists
        dataset_path = "../data/Dataset-salary-2024.csv"
        self.assertTrue(
            os.path.exists(dataset_path), f"Dataset file {dataset_path} does not exist."
        )

        # Run main function and capture output
        main()

        # Check if performance report file was created
        performance_report_path = "../python_performance.md"
        self.assertTrue(
            os.path.exists(performance_report_path),
            f"Performance report file {performance_report_path} was not created.",
        )

        # Read and verify performance report content
        with open(performance_report_path, "r") as f:
            content = f.read()
            self.assertIn("# Performance Report", content)
            self.assertIn("Time taken:", content)
            self.assertIn("Memory used:", content)
            self.assertIn("## Descriptive Statistics:", content)
            self.assertIn("## Top 20 Job Titles Distribution:", content)
            self.assertIn("## Experience Level Distribution:", content)
            self.assertIn("## Salary Statistics by Experience Level:", content)

        # Clean up the performance report file after test
        os.remove(performance_report_path)


if __name__ == "__main__":
    unittest.main()
