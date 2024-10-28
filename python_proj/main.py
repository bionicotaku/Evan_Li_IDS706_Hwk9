from mylib import calculate_stat
import time
import psutil
import io
from contextlib import redirect_stdout


def main():
    start_time = time.perf_counter()
    memory_before = psutil.virtual_memory().used / (1024.0)

    # Read data
    filteredData = calculate_stat.read_data("../data/Dataset-salary-2024.csv")

    # Calculate statistics
    stat = calculate_stat.calculate_stat(filteredData)
    job_title_counts = calculate_stat.calculate_job_title_distribution(filteredData)
    experience_level_counts = calculate_stat.calculate_experience_level_distribution(
        filteredData
    )
    salary_stats = calculate_stat.calculate_salary_stats_by_experience(filteredData)

    end_time = time.perf_counter()
    elapsed_time_micros = (end_time - start_time) * 1e6
    memory_after = psutil.virtual_memory().used / (1024.0)
    memory_used = memory_after - memory_before

    # Redirect output to a file
    with open("../python_performance.md", "w") as f:
        with redirect_stdout(f):
            print(f"# Performance Report\n")
            print(f"**Time taken:** {elapsed_time_micros:.2f} microseconds  ")
            print(f"**Memory used:** {memory_used:.2f} KB  \n")
            print("## Descriptive Statistics:")
            print("```")
            print(stat)
            print("```\n")
            print("## Top 20 Job Titles Distribution:")
            print("```")
            print(job_title_counts)
            print("```\n")
            print("## Experience Level Distribution:")
            print("```")
            print(experience_level_counts)
            print("```\n")
            print("## Salary Statistics by Experience Level:")
            print("```")
            print(salary_stats)
            print("```")


if __name__ == "__main__":
    main()
