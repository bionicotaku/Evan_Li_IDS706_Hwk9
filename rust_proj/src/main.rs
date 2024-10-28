use rust_proj::*;
use std::fs::File;
use std::io::Write;
use std::time::Instant;

fn main() {
    // Read data
    let filtered_data = read_data("../data/Dataset-salary-2024.csv").unwrap();

    let start_time = Instant::now();
    let mem_info_before = sys_info::mem_info().unwrap();

    // Calculate and print statistics
    let stat = calculate_stat(&filtered_data);
    let job_title_counts = calculate_job_title_distribution(&filtered_data);
    let experience_level_counts = calculate_experience_level_distribution(&filtered_data);

    // Calculate and print salary statistics by experience level
    let salary_stats = calculate_salary_stats_by_experience(&filtered_data);

    let end_time = Instant::now();
    let elapsed_time = end_time.duration_since(start_time);
    let mem_info_after = sys_info::mem_info().unwrap();
    let mem_used = mem_info_after.total - mem_info_before.total;

    let mut file = File::create("../rust_performance.md").expect("Unable to create file");

    writeln!(file, "# Analysis Results\n").expect("Unable to write to file");
    writeln!(file, "## Time and Memory Usage").expect("Unable to write to file");
    writeln!(
        file,
        "- Time taken: {:.2} microseconds",
        elapsed_time.as_micros()
    )
    .expect("Unable to write to file");
    writeln!(file, "- Memory used: {:.2} KB", mem_used).expect("Unable to write to file");

    writeln!(file, "\n## Descriptive Statistics").expect("Unable to write to file");
    writeln!(file, "{:?}", stat).expect("Unable to write to file");

    writeln!(file, "\n## Top 20 Job Titles Distribution").expect("Unable to write to file");
    writeln!(file, "{:?}", job_title_counts).expect("Unable to write to file");

    writeln!(file, "\n## Experience Level Distribution").expect("Unable to write to file");
    writeln!(file, "{:?}", experience_level_counts).expect("Unable to write to file");

    writeln!(file, "\n## Salary Statistics by Experience Level").expect("Unable to write to file");
    writeln!(file, "{:?}", salary_stats).expect("Unable to write to file");
}
