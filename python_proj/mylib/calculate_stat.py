import polars as pl

def read_data(file_path):
    # Read the data from the CSV file
    columns_to_keep = [
        "work_year",
        "experience_level",
        "job_title",
        "salary_in_usd",
        "remote_ratio",
        "company_size",
    ]
    return pl.read_csv(file_path).select(columns_to_keep)

def calculate_stat(data):
    # Calculate descriptive statistics of the data.
    return data.describe()

def calculate_job_title_distribution(data):
    job_title_counts = (data.group_by('job_title')
                        .agg(pl.len().alias('count'))
                        .sort('count', descending=True)
                        .head(20))
    return job_title_counts

def calculate_experience_level_distribution(data):
    experience_level_counts = (data.group_by('experience_level')
                               .agg(pl.len().alias('count'))
                               .sort('count', descending=True))
    return experience_level_counts

def calculate_salary_stats_by_experience(data):
    # Calculate salary statistics by experience level.
    return data.group_by('experience_level').agg([
        pl.col('salary_in_usd').count().alias('count'),
        pl.col('salary_in_usd').mean().alias('mean'),
        pl.col('salary_in_usd').median().alias('median'),
        pl.col('salary_in_usd').min().alias('min'),
        pl.col('salary_in_usd').max().alias('max')
    ])