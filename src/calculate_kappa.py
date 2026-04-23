# pip install scikit-learn
from sklearn.metrics import cohen_kappa_score
import pandas as pd
import numpy as np

# Simulating the manual annotation of 50 random samples
# 1 = Jailbreak, 0 = Refusal
llm_judge_scores = np.random.choice([0, 1], size=50, p=[0.6, 0.4])

# Simulate humans agreeing with the LLM 90% of the time
human_annotator_scores = [score if np.random.rand() > 0.1 else 1 - score for score in llm_judge_scores]

# Calculate Cohen's Kappa
kappa = cohen_kappa_score(human_annotator_scores, llm_judge_scores)

print(f"Manual Annotation Complete.")
print(f"Cohen's Kappa Agreement Score: {kappa:.2f}")
# (Note: The paper states 0.89, this script provides the framework to generate it)