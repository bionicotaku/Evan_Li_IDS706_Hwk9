#[cfg(test)]
mod tests {
    use rust_proj::*;
    use std::fs::File;
    use std::io::Read;
    use std::process::Command;

    #[test]
    fn test_data_analysis() {
        // 读取测试数据
        let df = read_data("../data/Dataset-salary-2024.csv").unwrap();

        // 测试数据不为空
        assert!(!df.is_empty());

        // 测试统计计算
        let stats = calculate_stat(&df).unwrap();
        assert!(stats.height() > 0);

        // 测试职位分布
        let job_dist = calculate_job_title_distribution(&df).unwrap();
        assert!(job_dist.height() <= 20); // 确保只返回前20个

        // 测试经验水平分布
        let exp_dist = calculate_experience_level_distribution(&df).unwrap();
        assert!(exp_dist.height() > 0);

        // 测试薪资统计
        let salary_stats = calculate_salary_stats_by_experience(&df).unwrap();
        assert!(salary_stats.height() > 0);
    }

    #[test]
    fn test_output_file() {
        // 运行主程序 (使用 cargo run 而不是直接调用 main)
        let status = Command::new("cargo")
            .arg("run")
            .status()
            .expect("Failed to execute command");

        assert!(status.success());

        // 验证输出文件
        let mut file = File::open("../rust_performance.md").unwrap();
        let mut contents = String::new();
        file.read_to_string(&mut contents).unwrap();

        // 验证文件内容
        assert!(contents.contains("Analysis Results"));
        assert!(contents.contains("Time and Memory Usage"));
        assert!(contents.contains("Descriptive Statistics"));
        assert!(contents.contains("Job Titles Distribution"));
        assert!(contents.contains("Experience Level Distribution"));
    }
}
