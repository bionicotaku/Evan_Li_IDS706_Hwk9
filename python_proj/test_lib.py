import pytest
import polars as pl
from mylib.calculate_stat import (
    read_data,
    calculate_salary_stats_by_experience,
)


# Sample data for testing
@pytest.fixture
def sample_data():
    return pl.DataFrame(
        {
            "work_year": [2020, 2021, 2022, 2023],
            "experience_level": ["EN", "MI", "SE", "EX"],
            "job_title": [
                "Data Analyst",
                "Software Engineer",
                "Data Scientist",
                "Manager",
            ],
            "salary_in_usd": [50000, 75000, 100000, 150000],
            "remote_ratio": [0, 50, 100, 100],
            "company_size": ["S", "M", "L", "L"],
        }
    )


def test_read_data(tmp_path):
    # Create a temporary CSV file
    df = pl.DataFrame(
        {
            "work_year": [2020, 2021],
            "experience_level": ["EN", "MI"],
            "job_title": ["Data Analyst", "Software Engineer"],
            "salary_in_usd": [50000, 75000],
            "remote_ratio": [0, 50],
            "company_size": ["S", "M"],
            "extra_column": [
                "A",
                "B",
            ],  # This column should not be included in the result
        }
    )
    file_path = tmp_path / "test.csv"
    df.write_csv(file_path)

    # Test reading the data
    result = read_data(file_path)
    assert isinstance(result, pl.DataFrame)
    assert result.columns == [
        "work_year",
        "experience_level",
        "job_title",
        "salary_in_usd",
        "remote_ratio",
        "company_size",
    ]
    assert "extra_column" not in result.columns


def test_calculate_salary_stats_by_experience(sample_data):
    result = calculate_salary_stats_by_experience(sample_data)
    assert isinstance(result, pl.DataFrame)
    assert set(result.columns) == set(
        ["experience_level", "count", "mean", "median", "min", "max"]
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
