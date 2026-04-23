import os
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd
import time 

# 1. Load the environment variables from the .env file
load_dotenv()

# 2. Setup the API client using the hidden key
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"), 
    base_url="https://api.groq.com/openai/v1",
)

# 3. Define Groq's newest active models
MODELS = {
    "Llama-3-8B": "llama-3.1-8b-instant",
    "Llama-3-70B": "llama-3.3-70b-versatile"
}

print("Loading full 250-prompt dataset...")
df = pd.read_csv("scriptural_bypass_dataset.csv")

results = []
total_prompts = len(df)

for index, row in df.iterrows():
    prompt = row['prompt']
    behavior = row['behavior_target']
    condition = row['condition']
    
    print(f"Processing Prompt {index + 1}/{total_prompts} - Condition: [{condition}]")
    
    for model_name, model_id in MODELS.items():
        try:
            response = client.chat.completions.create(
                model=model_id,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=250,
                temperature=0.7
            )
            output_text = response.choices[0].message.content.strip()
        except Exception as e:
            output_text = f"API_ERROR: {str(e)}"
            
        results.append({
            "model": model_name,
            "behavior_target": behavior,
            "condition": condition,
            "prompt": prompt,
            "response": output_text
        })
        
        # NEW: Pause for 2.5 seconds to prevent Groq from blocking us
        time.sleep(2.5) 

results_df = pd.DataFrame(results)
results_df.to_csv("inference_results.csv", index=False)
print(f"\nSuccess! Saved {len(results_df)} model responses to 'inference_results.csv'")