use polars::prelude::*;

pub fn read_data(file_path: &str) -> PolarsResult<DataFrame> {
    let df = CsvReader::from_path(file_path)?.has_header(true).finish()?;

    // Add validation
    if df.is_empty() {
        return Err(PolarsError::ComputeError("Empty dataset".into()));
    }

    df.lazy()
        .select([
            col("work_year"),
            col("experience_level"),
            col("job_title"),
            col("salary_in_usd"),
            col("remote_ratio"),
            col("company_size"),
        ])
        .filter(col("salary_in_usd").is_not_null()) // Filter out null salaries
        .collect()
}

pub fn calculate_stat(df: &DataFrame) -> PolarsResult<DataFrame> {
    // 移除 clone()，直接使用 describe
    df.describe(None)
}

pub fn calculate_job_title_distribution(df: &DataFrame) -> PolarsResult<DataFrame> {
    df.clone()
        .lazy() // 这里的 clone 是必须的
        .group_by([col("job_title")])
        .agg([count().alias("count")])
        .sort(
            "count",
            SortOptions {
                descending: true,
                nulls_last: true,
                multithreaded: true,
                maintain_order: false,
            },
        )
        .limit(20)
        .collect()
}

pub fn calculate_experience_level_distribution(df: &DataFrame) -> PolarsResult<DataFrame> {
    df.clone()
        .lazy()
        .group_by([col("experience_level")])
        .agg([count().alias("count")])
        .sort(
            "count",
            SortOptions {
                descending: true,
                nulls_last: true,
                multithreaded: true,
                maintain_order: false,
            },
        )
        .collect()
}

pub fn calculate_salary_stats_by_experience(df: &DataFrame) -> PolarsResult<DataFrame> {
    df.clone()
        .lazy()
        .group_by([col("experience_level")])
        .agg([
            count().alias("count"),
            col("salary_in_usd").mean().alias("mean"),
            col("salary_in_usd").median().alias("median"),
            col("salary_in_usd").min().alias("min"),
            col("salary_in_usd").max().alias("max"),
            col("salary_in_usd").std(1).alias("std_dev"), // Add standard deviation
        ])
        .sort(
            "mean",
            SortOptions {
                descending: true,
                nulls_last: true,
                multithreaded: true,
                maintain_order: false,
            },
        )
        .collect()
}
