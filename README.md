```markdown
# The Scriptural Bypass: Evaluating Semantic Adversarial Attacks via Religious Framing in LLMs

**Authors:** Pranav Reddy Sambidi, Adithya Vardhan Selvam, Sharath Talur Subramanian  
**Institution:** University of Florida  
**EGS6216/ CIS6930:** AI Ethics for Technology Leaders 

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
```

## Environment Setup

1. **Clone the repository:**
   ```bash
   git clone <YOUR_GITHUB_REPOSITORY_URL>
   cd ScripturalBypass
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the API Key:**
   This project uses the Groq API for high-throughput Llama-3 inference. You must provide your own API key to run the scripts.
   * Create a file named `.env` in the root directory.
   * Add your Groq API key to the file:
     ```env
     GROQ_API_KEY=your_api_key_here
     ```

## Execution Order for Reproducibility

To replicate the findings from our paper, run the scripts in the `src/` directory in the following chronological order:

**1. Generate the Dataset**
```bash
python src/generate_dataset.py
```
*Outputs `data/scriptural_bypass_dataset.csv` (250 prompts across 5 semantic conditions).*

**2. Run Model Inference**
```bash
python src/run_inference.py
```
*Queries the Llama-3 models via the Groq API. Includes a 2.5-second automated backoff to handle free-tier rate limits. Outputs `data/inference_results.csv`.*

**3. Evaluate the Responses (LLM-as-a-Judge)**
```bash
python src/evaluate_results.py
```
*Utilizes a strict rubric and a 0-temperature Llama-3 judge to calculate the Attack Success Rate (ASR). Outputs `data/evaluated_results.csv`.*

**4. Generate Visualizations**
```bash
python src/analyze_results.py
```
*Outputs the high-resolution comparative bar chart `visualizations/asr_results_chart.png`.*

**5. Test Defensive Mitigations**
```bash
python src/run_mitigation.py
```
*Re-runs the highly vulnerable conditions with a semantic-aware system prompt to test alignment recovery. Outputs `data/mitigated_results.csv`.*

**6. Validate the Judge**
```bash
python src/calculate_kappa.py
```
*Calculates the Cohen's Kappa ($\kappa$) coefficient to mathematically validate inter-rater reliability.*

## Key Findings
* **Severe Vulnerability:** The `Llama-3.3-70B` model exhibited a 70% Attack Success Rate (ASR) when harmful requests were framed as Biblical parables, compared to only 10% under Baseline conditions.
* **Inverse Scaling:** The larger, more capable 70B model was significantly more vulnerable to roleplay hijacking than the smaller 8B model.
* **Cultural Bias:** Models were highly accommodating to Western religious tropes (Biblical: 70%) but less fluid when bypasses were wrapped in non-Western epics (Mahabharata: 38%).

## Ethical Disclaimer
This research was conducted following responsible disclosure and ethical AI research guidelines. To minimize harm, the behaviors targeted in the generated dataset were strictly limited to "grey-area" sociological and digital harms (e.g., misinformation, social engineering). No prompts targeting physical violence or self-harm were included. The code and dataset provided in this repository are strictly for academic evaluation of model robustness and must not be used to conduct cyberattacks or malicious social engineering.
```