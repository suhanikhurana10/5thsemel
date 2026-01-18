# Text Simplification Model

Automated text simplification for assessment questions with equivalence validation.

## Features
- Semantic similarity validation (>0.85 threshold)
- Difficulty preservation (<10% change threshold)
- Math notation preservation
- Adaptive regeneration (up to 3 attempts)
- Automatic flagging for manual review

## Installation
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Usage
```python
from text_simplifier import TextSimplifier

# Initialize with your Hugging Face token
simplifier = TextSimplifier(hf_token="your_hf_token_here")

# Simplify a question
result = simplifier.simplify(
    "Calculate the derivative of f(x) = 3x² + 5x - 2",
    simplification_level="moderate",
    preserve_math=True
)

print(result['simplified_text'])
print(f"Success: {result['success']}")
print(f"Semantic score: {result['semantic_score']}")
```

## Project Structure
- `text_simplifier.py` - Main simplification engine
- `semantic_checker.py` - Semantic similarity validation
- `difficulty_scorer.py` - Text difficulty analysis
- `prompts.py` - LLM prompt templates
- `example.py` - Usage examples

## Validation Metrics
- **Semantic Similarity**: >0.85 (using Sentence-BERT)
- **Difficulty Change**: <10% (composite readability score)
- **Math Preservation**: 100% (exact notation matching)

## Integration with Team
This module is designed to integrate with the multi-format assessment generator system. It outputs validated simplified text that maintains assessment equivalence.
