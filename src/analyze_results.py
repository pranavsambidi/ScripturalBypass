import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the graded data
df = pd.read_csv("evaluated_results.csv")

# 2. Calculate ASR (Attack Success Rate)
asr_data = df.groupby(['model', 'condition'])['jailbreak_score'].mean().reset_index()
asr_data['jailbreak_score'] *= 100  # Convert to percentage

print("--- Attack Success Rates (ASR) ---")
print(asr_data.to_string(index=False))

# 3. Generate the Graph
plt.figure(figsize=(10, 6))
sns.barplot(data=asr_data, x='condition', y='jailbreak_score', hue='model', palette='viridis')

# 4. Format the chart to look academic (Perfect for ACL format)
plt.title('Attack Success Rate (ASR) by Semantic Framing Condition', fontsize=14, pad=15)
plt.ylabel('Attack Success Rate (%)', fontsize=12)
plt.xlabel('Semantic Prompt Condition', fontsize=12)
plt.ylim(0, 105)
plt.legend(title='Target Model')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# 5. Save the chart as a high-res image for your LaTeX paper
plt.savefig('asr_results_chart.png', dpi=300)
print("\nSuccess! Chart saved as 'asr_results_chart.png'.")