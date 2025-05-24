## Voice-to-Voice Sleep Agent

### Model
Using GPT-4o (voice-capable) via Chainlit frontend.

### Data Sources
- Apple Health / Fitbit / WHOOP sample data
- Research-based CSV on sleep quality

### Fine-tuning/Adaptation
Simulated adaptation with heuristics and data references from wearable & research data. Replace with actual fine-tuning logic in `fine_tune.py` if needed.

### Conversations
Check `examples/` for 5 example transcripts.

### Running
```
pip install -r requirements.txt
chainlit run app.py -w