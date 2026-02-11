#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
AI IMPACT ON STUDENT PERFORMANCE - COMPREHENSIVE ANALYSIS SYSTEM
================================================================================
Author: Abdul Wasay (FA22-BCS-127)
Course: Exploratory Data Analysis & Visualization (EDAV)
Purpose: Advanced analysis of AI tools impact on student academic performance
Version: 1.0
Python: 3.8+
Date: February 2026
================================================================================
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import warnings

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import pearsonr, spearmanr, chi2_contingency

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.gridspec import GridSpec
from matplotlib.ticker import FuncFormatter, PercentFormatter
import seaborn as sns

warnings.filterwarnings('ignore')
pd.options.mode.chained_assignment = None

# ============================================================================
# CONFIGURATION
# ============================================================================
class Config:
    """Configuration class for the analysis system"""
    INPUT_FILE = "ai_impact_student_performance_dataset.csv"
    OUTPUT_DIR = "outputs"
    FIGURE_DPI = 300
    FIGURE_FORMAT = 'png'
    COLOR_PALETTE_PRIMARY = "viridis"
    COLOR_PALETTE_SECONDARY = "Set2"
    STUDENT_NAME = "Abdul Wasay"
    STUDENT_ID = "FA22-BCS-127"
    COURSE_NAME = "Exploratory Data Analysis & Visualization"

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================
def setup_visualization_style():
    """Configure matplotlib and seaborn visual styles"""
    plt.style.use('default')
    sns.set_theme(style="whitegrid", font_scale=1.1)
    plt.rcParams.update({
        'figure.figsize': (12, 8),
        'figure.dpi': 100,
        'savefig.dpi': Config.FIGURE_DPI,
        'font.family': 'sans-serif',
        'axes.titlesize': 16,
        'axes.labelsize': 12,
        'legend.fontsize': 10,
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'grid.alpha': 0.3
    })

def print_header(title, char='=', width=80):
    """Print formatted section header"""
    print(f"\n{char * width}")
    print(f"{title.center(width)}")
    print(f"{char * width}\n")

def print_subheader(title, char='-', width=80):
    """Print formatted subsection header"""
    print(f"\n{title}")
    print(f"{char * width}")

def save_figure(filename):
    """Save figure with consistent settings"""
    filepath = os.path.join(Config.OUTPUT_DIR, filename)
    plt.savefig(filepath, dpi=Config.FIGURE_DPI, bbox_inches='tight', format=Config.FIGURE_FORMAT)
    print(f"  ✓ Saved: {filename}")

def create_output_directory():
    """Create output directory if it doesn't exist"""
    Path(Config.OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
    print(f"✓ Output directory ready: {Config.OUTPUT_DIR}")

# ============================================================================
# MAIN ANALYSIS FUNCTION
# ============================================================================
def main():
    """Main execution function"""
    
    # Print header
    print_header("AI IMPACT ON STUDENT PERFORMANCE - DATA ANALYSIS")
    print(f"Student: {Config.STUDENT_NAME} ({Config.STUDENT_ID})".center(80))
    print(f"Course: {Config.COURSE_NAME}".center(80))
    print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}".center(80))
    print("="*80 + "\n")
    
    # Setup
    setup_visualization_style()
    create_output_directory()
    
    # ============================================================================
    # DATA LOADING
    # ============================================================================
    print_header("DATA LOADING")
    
    try:
        df = pd.read_csv(Config.INPUT_FILE)
        print(f"✓ Dataset loaded successfully!")
        print(f"  • Records: {len(df):,}")
        print(f"  • Features: {len(df.columns)}")
        print(f"  • Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    except FileNotFoundError:
        print(f"✗ Error: File '{Config.INPUT_FILE}' not found!")
        print(f"  Please ensure the dataset is in the project directory.")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error loading data: {e}")
        sys.exit(1)
    
    # ============================================================================
    # DATA OVERVIEW
    # ============================================================================
    print_header("DATASET OVERVIEW")
    print("\nColumn Information:")
    print("-" * 80)
    for col in df.columns:
        dtype = df[col].dtype
        unique = df[col].nunique()
        missing = df[col].isnull().sum()
        print(f"  • {col:35s} | Type: {str(dtype):10s} | Unique: {unique:4d} | Missing: {missing}")
    
    # ============================================================================
    # DESCRIPTIVE STATISTICS
    # ============================================================================
    print_header("DESCRIPTIVE STATISTICS")
    
    print_subheader("Numerical Variables Summary")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print(df[numeric_cols].describe().round(2).to_string())
    
    print_subheader("AI Usage Statistics")
    ai_users = df['uses_ai'].sum()
    total = len(df)
    print(f"  • Total Students: {total:,}")
    print(f"  • AI Users: {ai_users:,} ({ai_users/total*100:.1f}%)")
    print(f"  • Non-AI Users: {total-ai_users:,} ({(total-ai_users)/total*100:.1f}%)")
    
    print_subheader("Performance Metrics")
    print(f"  • Average Final Score: {df['final_score'].mean():.2f}")
    print(f"  • Pass Rate: {df['passed'].sum()}/{len(df)} ({df['passed'].mean()*100:.1f}%)")
    high_perf = (df['performance_category']=='High').sum()
    print(f"  • High Performers: {high_perf} ({high_perf/len(df)*100:.1f}%)")
    
    # ============================================================================
    # VISUALIZATIONS
    # ============================================================================
    print_header("GENERATING VISUALIZATIONS")
    viz_count = 0
    
    # VIZ 1: AI Usage Distribution
    plt.figure(figsize=(12, 6))
    ai_counts = df['uses_ai'].value_counts()
    labels = ['Uses AI', 'Does Not Use AI']
    colors = ['#3498db', '#e74c3c']
    plt.pie(ai_counts.values, labels=labels, autopct='%1.1f%%', colors=colors, 
            startangle=90, explode=[0.05, 0], shadow=True,
            textprops={'fontsize': 14, 'weight': 'bold'})
    plt.title('AI Usage Distribution Among Students', fontsize=18, weight='bold', pad=20)
    plt.tight_layout()
    save_figure('01_ai_usage_distribution.png')
    plt.close()
    viz_count += 1
    
    # VIZ 2: Final Score Comparison
    plt.figure(figsize=(12, 7))
    ai_scores = df[df['uses_ai']==1]['final_score']
    non_ai_scores = df[df['uses_ai']==0]['final_score']
    
    bp = plt.boxplot([ai_scores, non_ai_scores], labels=['AI Users', 'Non-AI Users'],
                      patch_artist=True, showmeans=True, widths=0.6)
    bp['boxes'][0].set_facecolor('#3498db')
    bp['boxes'][1].set_facecolor('#e74c3c')
    for box in bp['boxes']:
        box.set_alpha(0.7)
    
    plt.title('Final Score Comparison: AI Users vs Non-AI Users', fontsize=18, weight='bold', pad=20)
    plt.ylabel('Final Score', fontsize=13, weight='bold')
    plt.grid(axis='y', alpha=0.3)
    
    # Add mean values
    for i, (pos, scores) in enumerate(zip([1, 2], [ai_scores, non_ai_scores])):
        mean_val = scores.mean()
        plt.text(pos, mean_val, f'μ={mean_val:.1f}', ha='center', va='bottom', 
                fontsize=11, weight='bold', color='darkred')
    
    plt.tight_layout()
    save_figure('02_final_score_ai_comparison.png')
    plt.close()
    viz_count += 1
    
    # VIZ 3: AI Tools Usage
    plt.figure(figsize=(14, 7))
    ai_tools = df[df['uses_ai']==1]['ai_tools_used'].value_counts()
    colors_tools = sns.color_palette('Set2', n_colors=len(ai_tools))
    bars = plt.bar(range(len(ai_tools)), ai_tools.values, color=colors_tools, 
                   edgecolor='black', alpha=0.8)
    plt.xticks(range(len(ai_tools)), ai_tools.index, rotation=45, ha='right')
    plt.title('Most Popular AI Tools Among Students', fontsize=18, weight='bold', pad=20)
    plt.ylabel('Number of Students', fontsize=13, weight='bold')
    plt.xlabel('AI Tools', fontsize=13, weight='bold')
    
    for i, v in enumerate(ai_tools.values):
        plt.text(i, v + max(ai_tools.values)*0.02, str(v), ha='center', 
                fontsize=11, weight='bold')
    
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    save_figure('03_ai_tools_popularity.png')
    plt.close()
    viz_count += 1
    
    # VIZ 4: AI Usage Purpose
    plt.figure(figsize=(12, 8))
    purposes = df[df['uses_ai']==1]['ai_usage_purpose'].value_counts()
    colors_purpose = sns.color_palette('pastel', n_colors=len(purposes))
    wedges, texts, autotexts = plt.pie(purposes.values, labels=purposes.index, 
                                         autopct='%1.1f%%', colors=colors_purpose, 
                                         startangle=45, shadow=True)
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontsize(12)
        autotext.set_weight('bold')
    
    plt.title('Purpose of AI Usage by Students', fontsize=18, weight='bold', pad=20)
    plt.tight_layout()
    save_figure('04_ai_usage_purpose.png')
    plt.close()
    viz_count += 1
    
    # VIZ 5: Performance Category Distribution
    plt.figure(figsize=(12, 7))
    perf_cat = df['performance_category'].value_counts()
    cat_colors = {'High': '#2ecc71', 'Medium': '#f39c12', 'Low': '#e74c3c'}
    bar_colors = [cat_colors.get(cat, '#95a5a6') for cat in perf_cat.index]
    
    bars = plt.barh(perf_cat.index, perf_cat.values, color=bar_colors, 
                    edgecolor='black', alpha=0.8)
    for i, v in enumerate(perf_cat.values):
        plt.text(v + max(perf_cat.values)*0.02, i, 
                f'{v} ({v/len(df)*100:.1f}%)', va='center', 
                fontsize=12, weight='bold')
    
    plt.title('Student Performance Category Distribution', fontsize=18, 
             weight='bold', pad=20)
    plt.xlabel('Number of Students', fontsize=13, weight='bold')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    save_figure('05_performance_distribution.png')
    plt.close()
    viz_count += 1
    
    # VIZ 6: Study Hours vs Final Score
    plt.figure(figsize=(12, 8))
    ai_data = df[df['uses_ai']==1]
    non_ai_data = df[df['uses_ai']==0]
    
    plt.scatter(ai_data['study_hours_per_day'], ai_data['final_score'], 
               label='AI Users', alpha=0.6, s=100, c='#3498db', 
               edgecolors='black', linewidth=0.5)
    plt.scatter(non_ai_data['study_hours_per_day'], non_ai_data['final_score'], 
               label='Non-AI Users', alpha=0.6, s=100, c='#e74c3c', 
               edgecolors='black', linewidth=0.5)
    
    # Trend lines
    if len(ai_data) > 1:
        z1 = np.polyfit(ai_data['study_hours_per_day'], ai_data['final_score'], 1)
        p1 = np.poly1d(z1)
        x_line = np.linspace(df['study_hours_per_day'].min(), 
                            df['study_hours_per_day'].max(), 100)
        plt.plot(x_line, p1(x_line), '--', color='#3498db', 
                linewidth=2, alpha=0.8, label='AI Trend')
    
    if len(non_ai_data) > 1:
        z2 = np.polyfit(non_ai_data['study_hours_per_day'], 
                       non_ai_data['final_score'], 1)
        p2 = np.poly1d(z2)
        plt.plot(x_line, p2(x_line), '--', color='#e74c3c', 
                linewidth=2, alpha=0.8, label='Non-AI Trend')
    
    plt.title('Study Hours vs Final Score (AI vs Non-AI)', 
             fontsize=18, weight='bold', pad=20)
    plt.xlabel('Study Hours Per Day', fontsize=13, weight='bold')
    plt.ylabel('Final Score', fontsize=13, weight='bold')
    plt.legend(fontsize=11, loc='best')
    plt.grid(alpha=0.3)
    plt.tight_layout()
    save_figure('06_study_hours_vs_score.png')
    plt.close()
    viz_count += 1
    
    # VIZ 7: AI Dependency Distribution
    plt.figure(figsize=(12, 7))
    ai_dep = df[df['uses_ai']==1]['ai_dependency_score']
    plt.hist(ai_dep, bins=10, color='#9b59b6', edgecolor='black', alpha=0.7)
    plt.axvline(ai_dep.mean(), color='red', linestyle='--', linewidth=2, 
               label=f'Mean: {ai_dep.mean():.1f}')
    plt.axvline(ai_dep.median(), color='green', linestyle='--', linewidth=2, 
               label=f'Median: {ai_dep.median():.1f}')
    
    plt.title('AI Dependency Score Distribution', fontsize=18, weight='bold', pad=20)
    plt.xlabel('AI Dependency Score (1-10)', fontsize=13, weight='bold')
    plt.ylabel('Frequency', fontsize=13, weight='bold')
    plt.legend(fontsize=11)
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    save_figure('07_ai_dependency_distribution.png')
    plt.close()
    viz_count += 1
    
    # VIZ 8: Attendance vs Performance
    plt.figure(figsize=(12, 8))
    plt.scatter(ai_data['attendance_percentage'], ai_data['final_score'], 
               label='AI Users', alpha=0.6, s=100, c='#3498db', edgecolors='black')
    plt.scatter(non_ai_data['attendance_percentage'], non_ai_data['final_score'], 
               label='Non-AI Users', alpha=0.6, s=100, c='#e74c3c', 
               edgecolors='black')
    
    plt.title('Attendance vs Final Score by AI Usage', 
             fontsize=18, weight='bold', pad=20)
    plt.xlabel('Attendance Percentage (%)', fontsize=13, weight='bold')
    plt.ylabel('Final Score', fontsize=13, weight='bold')
    plt.legend(fontsize=11)
    plt.grid(alpha=0.3)
    plt.tight_layout()
    save_figure('08_attendance_vs_score.png')
    plt.close()
    viz_count += 1
    
    # VIZ 9: Correlation Heatmap
    plt.figure(figsize=(14, 10))
    corr_cols = ['study_hours_per_day', 'ai_usage_time_minutes', 
                 'ai_dependency_score', 'last_exam_score', 'attendance_percentage', 
                 'concept_understanding_score', 'final_score']
    ai_numeric = ai_data[corr_cols].corr()
    mask = np.triu(np.ones_like(ai_numeric, dtype=bool))
    sns.heatmap(ai_numeric, annot=True, fmt='.2f', cmap='coolwarm', center=0, 
               square=True, linewidths=1, mask=mask, 
               cbar_kws={"shrink": 0.8}, vmin=-1, vmax=1)
    plt.title('Correlation Matrix - AI Users', fontsize=18, weight='bold', pad=20)
    plt.tight_layout()
    save_figure('09_correlation_heatmap_ai_users.png')
    plt.close()
    viz_count += 1
    
    # VIZ 10: Gender Performance
    plt.figure(figsize=(12, 7))
    gender_perf = df.groupby('gender')['final_score'].mean().sort_values(ascending=False)
    colors_gender = sns.color_palette('husl', n_colors=len(gender_perf))
    bars = plt.barh(gender_perf.index, gender_perf.values, color=colors_gender, 
                    edgecolor='black', alpha=0.8)
    
    for i, v in enumerate(gender_perf.values):
        plt.text(v + max(gender_perf.values)*0.02, i, f'{v:.1f}', 
                va='center', fontsize=12, weight='bold')
    
    plt.title('Average Final Score by Gender', fontsize=18, weight='bold', pad=20)
    plt.xlabel('Average Final Score', fontsize=13, weight='bold')
    plt.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    save_figure('10_gender_performance.png')
    plt.close()
    viz_count += 1
    
    # VIZ 11: Grade Level Performance
    plt.figure(figsize=(14, 7))
    grade_perf = df.groupby('grade_level')['final_score'].mean().sort_values(ascending=False)
    colors_grade = sns.color_palette('viridis', n_colors=len(grade_perf))
    bars = plt.bar(range(len(grade_perf)), grade_perf.values, 
                   color=colors_grade, edgecolor='black', alpha=0.8)
    plt.xticks(range(len(grade_perf)), grade_perf.index, rotation=45, ha='right')
    
    for i, v in enumerate(grade_perf.values):
        plt.text(i, v + 2, f'{v:.1f}', ha='center', fontsize=11, weight='bold')
    
    plt.title('Average Final Score by Grade Level', 
             fontsize=18, weight='bold', pad=20)
    plt.ylabel('Average Final Score', fontsize=13, weight='bold')
    plt.xlabel('Grade Level', fontsize=13, weight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    save_figure('11_grade_level_performance.png')
    plt.close()
    viz_count += 1
    
    # VIZ 12: Comprehensive Dashboard
    fig = plt.figure(figsize=(20, 14))
    gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)
    
    # Panel 1: AI Usage
    ax1 = fig.add_subplot(gs[0, 0])
    ai_counts_dash = df['uses_ai'].value_counts()
    ax1.pie(ai_counts_dash.values, labels=['Uses AI', 'No AI'], autopct='%1.1f%%',
           colors=['#3498db', '#e74c3c'], startangle=90)
    ax1.set_title('AI Usage', fontsize=14, weight='bold')
    
    # Panel 2: Performance Categories
    ax2 = fig.add_subplot(gs[0, 1])
    perf_cat_dash = df['performance_category'].value_counts()
    ax2.bar(range(len(perf_cat_dash)), perf_cat_dash.values, 
           color=['#2ecc71', '#f39c12', '#e74c3c'], alpha=0.8)
    ax2.set_xticks(range(len(perf_cat_dash)))
    ax2.set_xticklabels(perf_cat_dash.index, rotation=45)
    ax2.set_title('Performance Categories', fontsize=14, weight='bold')
    ax2.grid(axis='y', alpha=0.3)
    
    # Panel 3: Final Score Distribution
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.hist(df['final_score'], bins=20, color='#9b59b6', 
            edgecolor='black', alpha=0.7)
    ax3.axvline(df['final_score'].mean(), color='red', linestyle='--', linewidth=2)
    ax3.set_title('Final Score Distribution', fontsize=14, weight='bold')
    ax3.grid(axis='y', alpha=0.3)
    
    # Panel 4: AI Tools
    ax4 = fig.add_subplot(gs[1, :2])
    ai_tools_dash = df[df['uses_ai']==1]['ai_tools_used'].value_counts().head(5)
    ax4.barh(range(len(ai_tools_dash)), ai_tools_dash.values, 
            color=sns.color_palette('Set2', len(ai_tools_dash)))
    ax4.set_yticks(range(len(ai_tools_dash)))
    ax4.set_yticklabels(ai_tools_dash.index)
    ax4.set_title('Top 5 AI Tools Used', fontsize=14, weight='bold')
    ax4.grid(axis='x', alpha=0.3)
    
    # Panel 5: Study Hours vs Score
    ax5 = fig.add_subplot(gs[1, 2])
    ax5.scatter(df['study_hours_per_day'], df['final_score'], 
               alpha=0.5, c='#e67e22', s=50)
    ax5.set_title('Study Hours vs Score', fontsize=14, weight='bold')
    ax5.set_xlabel('Study Hours', fontsize=10)
    ax5.set_ylabel('Final Score', fontsize=10)
    ax5.grid(alpha=0.3)
    
    # Panel 6: Attendance Impact
    ax6 = fig.add_subplot(gs[2, 0])
    ax6.scatter(df['attendance_percentage'], df['final_score'], 
               alpha=0.5, c='#16a085', s=50)
    ax6.set_title('Attendance vs Score', fontsize=14, weight='bold')
    ax6.set_xlabel('Attendance %', fontsize=10)
    ax6.set_ylabel('Final Score', fontsize=10)
    ax6.grid(alpha=0.3)
    
    # Panel 7: Concept Understanding
    ax7 = fig.add_subplot(gs[2, 1])
    ax7.hist(df['concept_understanding_score'], bins=10, color='#c0392b', 
            edgecolor='black', alpha=0.7)
    ax7.set_title('Concept Understanding', fontsize=14, weight='bold')
    ax7.grid(axis='y', alpha=0.3)
    
    # Panel 8: Summary Stats
    ax8 = fig.add_subplot(gs[2, 2])
    ax8.axis('off')
    summary = f"""
SUMMARY STATISTICS

Total Students: {len(df):,}
AI Users: {ai_users:,} ({ai_users/total*100:.1f}%)
Avg Final Score: {df['final_score'].mean():.2f}
Pass Rate: {df['passed'].mean()*100:.1f}%
High Performers: {high_perf}
Avg Study Hours: {df['study_hours_per_day'].mean():.2f}
    """
    ax8.text(0.1, 0.5, summary, fontsize=11, family='monospace', 
            verticalalignment='center',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    fig.suptitle(f'AI Impact on Student Performance Dashboard\n{Config.STUDENT_NAME} ({Config.STUDENT_ID})',
                fontsize=20, weight='bold', y=0.995)
    plt.tight_layout()
    save_figure('12_comprehensive_dashboard.png')
    plt.close()
    viz_count += 1
    
    print(f"\n✓ Total visualizations generated: {viz_count}")
    
    # ============================================================================
    # STATISTICAL ANALYSIS
    # ============================================================================
    print_header("STATISTICAL ANALYSIS")
    
    print_subheader("Correlation Analysis - Key Findings")
    if len(ai_data) > 1:
        corr_ai = ai_data['ai_usage_time_minutes'].corr(ai_data['final_score'])
        print(f"  • AI Usage Time vs Final Score: r = {corr_ai:.3f}")
    
    corr_study = df['study_hours_per_day'].corr(df['final_score'])
    print(f"  • Study Hours vs Final Score: r = {corr_study:.3f}")
    
    corr_attend = df['attendance_percentage'].corr(df['final_score'])
    print(f"  • Attendance vs Final Score: r = {corr_attend:.3f}")
    
    print_subheader("T-Test: AI Users vs Non-AI Users")
    t_stat, p_value = stats.ttest_ind(ai_scores, non_ai_scores)
    print(f"  • AI Users Mean: {ai_scores.mean():.2f}")
    print(f"  • Non-AI Users Mean: {non_ai_scores.mean():.2f}")
    print(f"  • T-statistic: {t_stat:.3f}")
    print(f"  • P-value: {p_value:.4f}")
    if p_value < 0.05:
        print(f"  • Result: Significant difference (p < 0.05)")
    else:
        print(f"  • Result: No significant difference (p ≥ 0.05)")
    
    # ============================================================================
    # KEY INSIGHTS
    # ============================================================================
    print_header("KEY INSIGHTS & RECOMMENDATIONS")
    
    print_subheader("📊 MAIN FINDINGS")
    print(f"  1. AI Adoption Rate: {ai_users/total*100:.1f}% of students use AI tools")
    print(f"  2. Average Final Score: {df['final_score'].mean():.2f}")
    print(f"  3. Pass Rate: {df['passed'].mean()*100:.1f}%")
    print(f"  4. High Performers: {high_perf} students ({high_perf/len(df)*100:.1f}%)")
    
    print_subheader("🤖 AI USAGE INSIGHTS")
    most_popular_tool = df[df['uses_ai']==1]['ai_tools_used'].value_counts().idxmax()
    most_common_purpose = df[df['uses_ai']==1]['ai_usage_purpose'].value_counts().idxmax()
    print(f"  • Most Popular AI Tool: {most_popular_tool}")
    print(f"  • Most Common Purpose: {most_common_purpose}")
    if len(ai_data) > 0:
        print(f"  • Average AI Dependency Score: {ai_data['ai_dependency_score'].mean():.2f}/10")
    
    print_subheader("🎯 PERFORMANCE COMPARISON")
    print(f"  • AI Users Avg Score: {ai_scores.mean():.2f}")
    print(f"  • Non-AI Users Avg Score: {non_ai_scores.mean():.2f}")
    print(f"  • Difference: {abs(ai_scores.mean() - non_ai_scores.mean()):.2f} points")
    
    print_subheader("🔍 RECOMMENDATIONS")
    print(f"  1. Encourage balanced AI usage with traditional study methods")
    print(f"  2. Focus on improving attendance (current avg: {df['attendance_percentage'].mean():.1f}%)")
    if len(ai_data) > 0:
        print(f"  3. Promote ethical AI usage (avg ethics score: {ai_data['ai_ethics_score'].mean():.2f}/10)")
    print(f"  4. Provide AI literacy training for students")
    print(f"  5. Monitor AI dependency to prevent over-reliance")
    
    print_header("ANALYSIS COMPLETE!")
    print(f"✓ Total Records Analyzed: {len(df):,}")
    print(f"✓ Total Visualizations: {viz_count}")
    print(f"✓ Output Directory: {Config.OUTPUT_DIR}")
    print("="*80 + "\n")
    print("Thank you for using the AI Impact Analysis System!".center(80))
    print("="*80 + "\n")

# ============================================================================
# SCRIPT ENTRY POINT
# ============================================================================
if __name__ == "__main__":
    main()
