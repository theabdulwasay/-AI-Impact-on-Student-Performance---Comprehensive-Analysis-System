# 🤖 AI Impact on Student Performance - Comprehensive Analysis System

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Data Science](https://img.shields.io/badge/domain-Education%20Analytics-orange.svg)]()

> **Advanced statistical analysis and visualization of AI tools' impact on student academic performance**

A comprehensive Python-based analytical system designed to explore how artificial intelligence tools influence student learning outcomes, study patterns, and academic success. Built for the EDAV course with production-ready code and extensive visualizations.

---

## 🎯 Project Overview

This project analyzes a dataset of 8,000 students to understand:
- **AI Adoption Patterns**: Who uses AI and why?
- **Performance Metrics**: Does AI usage correlate with better grades?
- **Study Behaviors**: How AI affects study hours, attendance, and engagement
- **Tool Preferences**: Which AI tools are most popular among students?
- **Ethical Considerations**: AI dependency and ethical usage patterns

---

## ✨ Key Features

### 📊 Data Analysis Capabilities
- ✅ **Comprehensive Dataset Analysis** - 8,000 students, 26 features
- ✅ **AI Usage Profiling** - Detailed breakdown of AI tool adoption
- ✅ **Performance Comparison** - AI users vs non-AI users
- ✅ **Correlation Analysis** - Statistical relationships between variables
- ✅ **Hypothesis Testing** - T-tests and significance testing
- ✅ **Distribution Analysis** - Normality tests, quartiles, outliers

### 📈 Visualizations (12 Types)
1. **AI Usage Distribution** - Pie chart showing adoption rate
2. **Final Score Comparison** - Box plots comparing AI vs non-AI users
3. **AI Tools Popularity** - Bar chart of most used tools
4. **AI Usage Purpose** - Pie chart of primary use cases
5. **Performance Distribution** - Category breakdown (High/Medium/Low)
6. **Study Hours vs Score** - Scatter plots with trend lines
7. **AI Dependency Distribution** - Histogram of dependency scores
8. **Attendance vs Score** - Relationship analysis
9. **Correlation Heatmap** - AI users' key metrics
10. **Gender Performance** - Average scores by gender
11. **Grade Level Performance** - Analysis across education levels
12. **Comprehensive Dashboard** - Multi-panel overview

### 🔍 Statistical Insights
- Correlation coefficients (Pearson's r)
- Independent t-tests
- Descriptive statistics (mean, median, std dev)
- Performance category distributions
- AI dependency metrics

---

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Dataset Description](#dataset-description)
- [Usage](#usage)
- [Analysis Results](#analysis-results)
- [Project Structure](#project-structure)
- [Key Findings](#key-findings)
- [Visualizations](#visualizations)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 500 MB free disk space

### Step 1: Clone Repository
```bash
git clone https://github.com/abdulwasay/ai-impact-student-performance.git
cd ai-impact-student-performance
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Verify Installation
```bash
python --version  # Should show Python 3.8+
pip list  # Verify pandas, numpy, matplotlib, seaborn, scipy
```

---

## ⚡ Quick Start

### Basic Usage
```bash
python ai_impact_analysis.py
```

All visualizations will be saved to `/mnt/user-data/outputs/`

### Using Your Own Dataset
```python
# Place your CSV file in the project directory
# Update Config.INPUT_FILE path
python ai_impact_analysis.py
```

---

## 📊 Dataset Description

### Overview
- **Total Records**: 8,000 students
- **Features**: 26 variables
- **Data Size**: 3.33 MB
- **Data Type**: CSV format

### Key Features

| Feature | Type | Description | Example |
|---------|------|-------------|---------|
| `student_id` | integer | Unique identifier | 1, 2, 3... |
| `age` | integer | Student age | 14-24 years |
| `gender` | string | Gender | Male, Female, Other |
| `grade_level` | string | Education level | 10th, 11th, 12th, 1st Year, 3rd Year |
| `study_hours_per_day` | float | Daily study time | 0.5-6.0 hours |
| `uses_ai` | boolean | AI usage flag | 0 (No), 1 (Yes) |
| `ai_usage_time_minutes` | integer | Minutes using AI | 0-179 minutes |
| `ai_tools_used` | string | Tools utilized | ChatGPT, Gemini, Copilot |
| `ai_usage_purpose` | string | Primary purpose | Homework, Exam Prep, Coding |
| `ai_dependency_score` | integer | Dependency level | 1-10 scale |
| `ai_generated_content_percentage` | integer | AI content % | 0-100% |
| `ai_prompts_per_week` | integer | Weekly prompts | 0-119 |
| `ai_ethics_score` | integer | Ethical usage | 1-10 scale |
| `last_exam_score` | integer | Recent exam | 20-99 |
| `assignment_scores_avg` | float | Assignment avg | 30-100 |
| `attendance_percentage` | float | Attendance rate | 40-100% |
| `concept_understanding_score` | integer | Understanding level | 1-10 |
| `study_consistency_index` | float | Study regularity | 1-10 |
| `improvement_rate` | float | Progress rate | -20 to 40 |
| `sleep_hours` | float | Sleep per night | 4-9 hours |
| `social_media_hours` | float | Social media time | 0-6 hours |
| `tutoring_hours` | float | Tutoring received | 0-5 hours |
| `class_participation_score` | integer | Participation level | 1-10 |
| `final_score` | float | Final grade | 12.7-95.8 |
| `passed` | boolean | Pass/Fail status | 0 (Fail), 1 (Pass) |
| `performance_category` | string | Performance tier | High, Medium, Low |

---

## 💻 Usage

### Method 1: Command Line
```bash
python ai_impact_analysis.py
```

### Method 2: Python Script
```python
from ai_impact_analysis import *

# Load data
df = pd.read_csv('ai_impact_student_performance_dataset.csv')

# Run analysis
setup_visualization_style()
generate_all_visualizations(df)
perform_statistical_analysis(df)
```

### Method 3: Jupyter Notebook
```python
# See example_analysis.ipynb for interactive analysis
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv('ai_impact_student_performance_dataset.csv')
# ... continue with analysis
```

---

## 📈 Analysis Results

### Key Statistics

#### Overall Performance
- **Total Students**: 8,000
- **Average Final Score**: 56.81 / 100
- **Pass Rate**: 88.9% (7,114 students)
- **High Performers**: 9.4% (753 students)

#### AI Adoption
- **AI Users**: 64.1% (5,128 students)
- **Non-AI Users**: 35.9% (2,872 students)
- **Most Popular Tool**: ChatGPT+Gemini
- **Primary Purpose**: Exam Preparation

#### Performance Comparison
- **AI Users Avg Score**: 56.80
- **Non-AI Users Avg Score**: 56.84
- **Difference**: 0.05 points (NOT statistically significant, p=0.88)

#### Study Patterns
- **Average Study Hours**: 3.29 hours/day
- **Average Attendance**: 69.9%
- **Average AI Dependency**: 5.54 / 10
- **Average Sleep**: 6.47 hours/night

---

## 🔍 Key Findings

### 1. AI Adoption is High but Impact is Neutral
- 64.1% of students use AI tools
- No significant difference in final scores between AI users and non-users (p=0.88)
- **Implication**: AI is a tool, not a silver bullet

### 2. ChatGPT+Gemini Dominates
- Most popular combination of AI tools
- Used primarily for exam preparation
- Students combine multiple tools for better results

### 3. AI Dependency Varies Widely
- Average dependency score: 5.54/10
- Wide distribution from minimal to heavy reliance
- **Concern**: Some students may be over-dependent

### 4. Study Hours Matter More
- Correlation between study hours and final score exists
- AI usage time shows near-zero correlation with scores
- **Takeaway**: Traditional study still essential

### 5. Attendance Remains Critical
- Average attendance is only 69.9% - room for improvement
- Weak correlation with AI usage
- **Recommendation**: Focus on attendance improvement

### 6. Ethical Concerns
- Average ethics score: 5.46/10 (moderate)
- Need for better AI literacy education
- Students may not fully understand ethical implications

---

## 📊 Visualizations

All visualizations are generated at 300 DPI for publication quality.

### Sample Outputs

#### 1. AI Usage Distribution
Shows 64.1% adoption rate with clear visual breakdown

#### 2. Performance Comparison
Box plots revealing similar distributions between groups

#### 3. Tool Popularity
Bar charts highlighting ChatGPT+Gemini dominance

#### 4. Comprehensive Dashboard
12-panel overview providing complete analytical perspective

---

## 🏗️ Project Structure

```
ai-impact-student-performance/
│
├── ai_impact_analysis.py          # Main analysis script
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── LICENSE                         # MIT License
├── INSTALLATION.md                 # Detailed setup guide
├── .gitignore                      # Git ignore rules
│
├── data/
│   └── ai_impact_student_performance_dataset.csv  # Input data
│
├── outputs/                        # Generated visualizations
│   ├── 01_ai_usage_distribution.png
│   ├── 02_final_score_ai_comparison.png
│   ├── 03_ai_tools_popularity.png
│   ├── 04_ai_usage_purpose.png
│   ├── 05_performance_distribution.png
│   ├── 06_study_hours_vs_score.png
│   ├── 07_ai_dependency_distribution.png
│   ├── 08_attendance_vs_score.png
│   ├── 09_correlation_heatmap_ai_users.png
│   ├── 10_gender_performance.png
│   ├── 11_grade_level_performance.png
│   └── 12_comprehensive_dashboard.png
│
├── notebooks/
│   └── example_analysis.ipynb     # Jupyter notebook demo
│
└── docs/
    ├── methodology.md              # Analysis methodology
    └── findings.md                 # Detailed findings report
```

---

## 📚 Dependencies

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.2
scipy>=1.7.0
```

---

## 🔬 Methodology

### Statistical Tests Used
1. **Descriptive Statistics**: Mean, median, standard deviation, quartiles
2. **Correlation Analysis**: Pearson's r for relationships
3. **Hypothesis Testing**: Independent t-tests for group comparisons
4. **Distribution Analysis**: Histograms, box plots, violin plots

### Significance Level
- α = 0.05 (95% confidence level)
- P-values reported for all hypothesis tests

---

## 🎯 Recommendations

### For Students
1. **Balance AI with Traditional Study**: AI is a supplement, not a replacement
2. **Focus on Fundamentals**: Study hours still matter most
3. **Improve Attendance**: Current 69.9% average is too low
4. **Use AI Ethically**: Understand proper use cases
5. **Avoid Over-Dependence**: Maintain critical thinking skills

### For Educators
1. **Provide AI Literacy Training**: Help students use tools effectively
2. **Monitor AI Dependency**: Watch for over-reliance
3. **Promote Ethical Usage**: Establish clear guidelines
4. **Encourage Attendance**: Focus on engagement strategies
5. **Track Performance Patterns**: Regular assessment of AI impact

### For Institutions
1. **Develop AI Policies**: Clear rules for academic integrity
2. **Invest in Training**: Both students and faculty
3. **Research Impact**: Ongoing monitoring of AI effects
4. **Support Infrastructure**: Ensure equitable access
5. **Collaborate with AI Companies**: Educational partnerships

---

## 🤝 Contributing

Contributions welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Guidelines
- Follow PEP 8 style
- Add tests for new features
- Update documentation
- Ensure all tests pass

---

## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Abdul Wasay**
- Student ID: FA22-BCS-127
- Course: Exploratory Data Analysis & Visualization (EDAV)
- Institution: [Your University Name]
- Email: abdul.wasay@example.com
- GitHub: [@abdulwasay](https://github.com/abdulwasay)
- LinkedIn: [Abdul Wasay](https://linkedin.com/in/abdulwasay)

---

## 🙏 Acknowledgments

- Course instructor and teaching assistants
- Fellow students for dataset discussions
- Python data science community
- Matplotlib, Seaborn, and Pandas contributors
- AI tools (ChatGPT, Gemini, Copilot) for analysis assistance

---

## 📖 Citation

If you use this analysis in your research, please cite:

```bibtex
@misc{wasay2026aiimpact,
  author = {Wasay, Abdul},
  title = {AI Impact on Student Performance: Comprehensive Analysis System},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/abdulwasay/ai-impact-student-performance}}
}
```

---

## 📊 Research Questions Addressed

1. **Does AI usage improve academic performance?**
   - Finding: No significant difference (p=0.88)
   
2. **Which AI tools are most popular?**
   - Finding: ChatGPT+Gemini (combined usage)
   
3. **What drives AI adoption?**
   - Finding: Exam preparation is primary motivator
   
4. **Is there AI dependency concern?**
   - Finding: Moderate dependency (avg 5.54/10)
   
5. **How does AI affect study patterns?**
   - Finding: Minimal correlation with traditional metrics

---

## 🔮 Future Work

### Planned Enhancements
- [ ] Longitudinal study tracking same students over time
- [ ] Machine learning predictions of performance
- [ ] Natural language processing of student feedback
- [ ] Interactive dashboard (Plotly/Dash)
- [ ] Real-time data collection system
- [ ] Multi-institution comparison
- [ ] Qualitative interviews with students
- [ ] Cost-benefit analysis of AI adoption

---

## ❓ FAQ

**Q: Can I use this with my own dataset?**  
A: Yes! Just ensure your CSV has similar columns and update the file path.

**Q: How do I interpret the correlation values?**  
A: r > 0.7: Strong, 0.3-0.7: Moderate, <0.3: Weak. Check p-values for significance.

**Q: What does "no significant difference" mean?**  
A: Statistically, we cannot say AI users perform better than non-AI users (p=0.88 > 0.05).

**Q: Why is the analysis showing neutral AI impact?**  
A: Many factors affect performance. AI is just one tool among many (study habits, attendance, etc.).

**Q: Can I modify the visualizations?**  
A: Absolutely! All code is open-source. Edit the plotting sections as needed.

**Q: How do I add more statistical tests?**  
A: Use scipy.stats library. Add tests in the statistical analysis section.

---

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐ on GitHub!

---

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/abdulwasay/ai-impact-student-performance/issues)
- **Discussions**: [GitHub Discussions](https://github.com/abdulwasay/ai-impact-student-performance/discussions)
- **Email**: abdul.wasay@example.com

---

<div align="center">

**Built with ❤️ for Education Analytics**

*Abdul Wasay (FA22-BCS-127)*  
*Exploratory Data Analysis & Visualization Course*

[⬆ Back to Top](#-ai-impact-on-student-performance---comprehensive-analysis-system)

</div>
