# The Scriptural Bypass: Evaluating Semantic Adversarial Attacks via Religious Framing in LLMs

**Authors:** Pranav Reddy Sambidi, Adithya Vardhan Selvam, Sharath Talur Subramanian  
**Institution:** University of Florida  
**Track:** AI Ethics and Safety  

## Project Overview
Modern Large Language Models (LLMs) utilize Reinforcement Learning from Human Feedback (RLHF) to align against generating harmful content. While these filters successfully block direct malicious requests, this project exposes a critical vulnerability called the **Scriptural Bypass**. We demonstrate that AI safety filters can be easily bypassed by disguising harmful requests (e.g., phishing scams, misinformation) as ancient religious texts, mythology, or historical scripture. 

This repository contains the complete dataset, inference pipeline, and automated evaluation code used to test this vulnerability against the `Llama-3.1-8B` and `Llama-3.3-70B` models.

## Repository Architecture

```text
ScripturalBypass/
├── data/
│   ├── scriptural_bypass_dataset.csv
│   ├── inference_results.csv
│   ├── evaluated_results.csv
│   └── mitigated_results.csv
├── src/
│   ├── generate_dataset.py
│   ├── run_inference.py
│   ├── evaluate_results.py
│   ├── run_mitigation.py
│   └── calculate_kappa.py
├── visualizations/
│   └── asr_results_chart.png
├── paper/
│   └── TheScripturalBypass.pdf
├── .gitignore
├── requirements.txt
└── README.md