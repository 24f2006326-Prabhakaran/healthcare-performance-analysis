"""
Healthcare Performance Analysis - Patient Satisfaction Analysis
Author: 24f2006326@ds.study.iitm.ac.in
Date: December 2024

This script analyzes quarterly patient satisfaction scores and generates
visualizations to support strategic decision-making.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

class HealthcareAnalyzer:
    """
    A comprehensive analyzer for healthcare patient satisfaction metrics.
    """
    
    def __init__(self):
        """Initialize the analyzer with quarterly data."""
        self.quarters = ['Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
        self.scores = [2.32, -0.48, 8.2, 6.07]
        self.target = 4.5
        self.average = None
        self.df = None
        self._prepare_data()
    
    def _prepare_data(self):
        """Prepare the data for analysis."""
        self.df = pd.DataFrame({
            'Quarter': self.quarters,
            'Satisfaction_Score': self.scores,
            'Target': [self.target] * len(self.quarters)
        })
        
        # Calculate average
        self.average = np.mean(self.scores)
        print(f"Average Patient Satisfaction Score: {self.average:.2f}")
        print(f"Industry Target: {self.target}")
        print(f"Gap to Target: {self.target - self.average:.2f}")
    
    def generate_summary_statistics(self):
        """Generate comprehensive summary statistics."""
        print("\n" + "="*60)
        print("SUMMARY STATISTICS")
        print("="*60)
        
        stats = {
            'Average Score': self.average,
            'Minimum Score': min(self.scores),
            'Maximum Score': max(self.scores),
            'Range': max(self.scores) - min(self.scores),
            'Standard Deviation': np.std(self.scores),
            'Variance': np.var(self.scores),
            'Gap to Target': self.target - self.average
        }
        
        for key, value in stats.items():
            print(f"{key:.<40} {value:.2f}")
        
        return stats
    
    def plot_trend_analysis(self, save_path='trend_analysis.png'):
        """Create a comprehensive trend analysis visualization."""
        fig, ax = plt.subplots(figsize=(12, 7))
        
        # Plot the actual scores
        ax.plot(self.quarters, self.scores, marker='o', linewidth=2.5, 
                markersize=10, label='Actual Satisfaction Score', color='#3498db')
        
        # Plot the target line
        ax.axhline(y=self.target, color='#2ecc71', linestyle='--', 
                   linewidth=2, label=f'Industry Target ({self.target})')
        
        # Plot the average line
        ax.axhline(y=self.average, color='#e74c3c', linestyle='--', 
                   linewidth=2, label=f'Current Average ({self.average:.2f})')
        
        # Highlight problem areas
        for i, score in enumerate(self.scores):
            if score < self.target:
                ax.scatter(self.quarters[i], score, s=200, c='red', 
                          alpha=0.3, zorder=5)
        
        # Formatting
        ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
        ax.set_ylabel('Satisfaction Score', fontsize=12, fontweight='bold')
        ax.set_title('Quarterly Patient Satisfaction Trend Analysis\nCurrent Average: 4.03 | Target: 4.5', 
                     fontsize=14, fontweight='bold', pad=20)
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, alpha=0.3)
        
        # Add value labels on points
        for i, (quarter, score) in enumerate(zip(self.quarters, self.scores)):
            ax.annotate(f'{score:.2f}', 
                       xy=(quarter, score), 
                       xytext=(0, 10), 
                       textcoords='offset points',
                       ha='center',
                       fontsize=9,
                       fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\nTrend analysis saved to: {save_path}")
        plt.close()
    
    def plot_comparison_chart(self, save_path='comparison_chart.png'):
        """Create a bar chart comparing actual vs target scores."""
        fig, ax = plt.subplots(figsize=(12, 7))
        
        x = np.arange(len(self.quarters))
        width = 0.35
        
        # Create bars
        bars1 = ax.bar(x - width/2, self.scores, width, 
                       label='Actual Score', color='#3498db', alpha=0.8)
        bars2 = ax.bar(x + width/2, [self.target]*len(self.quarters), width, 
                       label='Target Score', color='#2ecc71', alpha=0.8)
        
        # Color bars below target in red
        for i, (bar, score) in enumerate(zip(bars1, self.scores)):
            if score < self.target:
                bar.set_color('#e74c3c')
        
        # Formatting
        ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
        ax.set_ylabel('Satisfaction Score', fontsize=12, fontweight='bold')
        ax.set_title('Actual vs Target Patient Satisfaction Scores\nAverage: 4.03 | Target: 4.5', 
                     fontsize=14, fontweight='bold', pad=20)
        ax.set_xticks(x)
        ax.set_xticklabels(self.quarters)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax.annotate(f'{height:.2f}',
                           xy=(bar.get_x() + bar.get_width() / 2, height),
                           xytext=(0, 3),
                           textcoords="offset points",
                           ha='center', va='bottom',
                           fontsize=9, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Comparison chart saved to: {save_path}")
        plt.close()
    
    def plot_gap_analysis(self, save_path='gap_analysis.png'):
        """Create a visualization showing the gap to target for each quarter."""
        fig, ax = plt.subplots(figsize=(12, 7))
        
        gaps = [score - self.target for score in self.scores]
        colors = ['#2ecc71' if gap >= 0 else '#e74c3c' for gap in gaps]
        
        bars = ax.bar(self.quarters, gaps, color=colors, alpha=0.7, edgecolor='black')
        
        # Add zero line
        ax.axhline(y=0, color='black', linestyle='-', linewidth=1)
        
        # Formatting
        ax.set_xlabel('Quarter', fontsize=12, fontweight='bold')
        ax.set_ylabel('Gap to Target (Score - 4.5)', fontsize=12, fontweight='bold')
        ax.set_title('Performance Gap Analysis by Quarter\nNegative = Below Target | Positive = Above Target', 
                     fontsize=14, fontweight='bold', pad=20)
        ax.grid(True, alpha=0.3, axis='y')
        
        # Add value labels
        for bar, gap in zip(bars, gaps):
            height = bar.get_height()
            ax.annotate(f'{gap:.2f}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3 if height > 0 else -15),
                       textcoords="offset points",
                       ha='center', va='bottom' if height > 0 else 'top',
                       fontsize=10, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Gap analysis saved to: {save_path}")
        plt.close()
    
    def generate_insights(self):
        """Generate key insights from the analysis."""
        print("\n" + "="*60)
        print("KEY INSIGHTS & FINDINGS")
        print("="*60)
        
        insights = [
            f"1. CURRENT PERFORMANCE: Average satisfaction score is {self.average:.2f}, "
            f"which is {self.target - self.average:.2f} points below the industry target of {self.target}.",
            
            f"\n2. EXTREME VOLATILITY: Scores range from {min(self.scores):.2f} to {max(self.scores):.2f}, "
            f"indicating highly inconsistent service delivery across quarters.",
            
            f"\n3. CRITICAL CONCERN: Q2 2024 showed a negative satisfaction score (-0.48), "
            f"suggesting severe service failures and potential crisis situations.",
            
            f"\n4. PROVEN CAPABILITY: Q3 2024 achieved an exceptional score of 8.2, "
            f"demonstrating that the organization CAN exceed targets when properly managed.",
            
            f"\n5. BUSINESS IMPACT: Below-target performance risks patient retention, "
            f"regulatory compliance, and revenue generation."
        ]
        
        for insight in insights:
            print(insight)
        
        return insights
    
    def generate_recommendations(self):
        """Generate actionable recommendations."""
        print("\n" + "="*60)
        print("STRATEGIC RECOMMENDATIONS")
        print("="*60)
        
        recommendations = [
            "\n🎯 PRIMARY SOLUTION: Improve service quality and wait times",
            "\n1. CRITICAL - REDUCE WAIT TIMES (0-3 months)",
            "   • Implement triage optimization system",
            "   • Expand urgent care capacity",
            "   • Target: 30% reduction in average wait time",
            "   • Expected Impact: +0.3 to +0.5 score improvement",
            
            "\n2. CRITICAL - ENHANCE SERVICE QUALITY (0-6 months)",
            "   • Launch comprehensive staff training program",
            "   • Focus on patient communication and bedside manner",
            "   • Implement quality assurance protocols",
            "   • Expected Impact: +0.2 to +0.4 score improvement",
            
            "\n3. HIGH PRIORITY - STANDARDIZE CARE DELIVERY (3-6 months)",
            "   • Develop consistent care protocols across departments",
            "   • Reduce performance volatility",
            "   • Implement best practices from Q3 2024 success",
            "   • Expected Impact: Sustained performance above 4.5",
            
            "\n4. MEDIUM PRIORITY - REAL-TIME FEEDBACK (1-3 months)",
            "   • Deploy digital feedback collection at point-of-care",
            "   • Enable immediate issue identification and resolution",
            "   • Create accountability dashboards",
            "   • Expected Impact: Faster problem detection and resolution"
        ]
        
        for rec in recommendations:
            print(rec)
        
        print("\n" + "="*60)
        print("EXPECTED OUTCOMES")
        print("="*60)
        print("• 3 Months:  Score improvement to 4.2-4.3")
        print("• 6 Months:  Achieve target of 4.5+")
        print("• 12 Months: Sustained performance at 4.7+")
        
        return recommendations
    
    def run_full_analysis(self):
        """Execute the complete analysis pipeline."""
        print("\n" + "="*60)
        print("HEALTHCARE PERFORMANCE ANALYSIS")
        print("Contact: 24f2006326@ds.study.iitm.ac.in")
        print("="*60)
        
        # Generate statistics
        self.generate_summary_statistics()
        
        # Generate visualizations
        print("\nGenerating visualizations...")
        self.plot_trend_analysis()
        self.plot_comparison_chart()
        self.plot_gap_analysis()
        
        # Generate insights and recommendations
        self.generate_insights()
        self.generate_recommendations()
        
        print("\n" + "="*60)
        print("Analysis complete! All visualizations have been saved.")
        print("="*60)


if __name__ == "__main__":
    # Initialize and run the analyzer
    analyzer = HealthcareAnalyzer()
    analyzer.run_full_analysis()
    
    print("\n✅ Analysis completed successfully!")
    print("📊 Review the generated visualizations:")
    print("   - trend_analysis.png")
    print("   - comparison_chart.png")
    print("   - gap_analysis.png")
    print("\n📧 Contact: 24f2006326@ds.study.iitm.ac.in")
