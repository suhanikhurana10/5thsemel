"""
Example usage of the text simplification system.
"""

from text_simplifier import TextSimplifier
import os

# Initialize (you need a Hugging Face token)
HF_TOKEN = os.getenv("HF_TOKEN")  # Set this environment variable
simplifier = TextSimplifier(hf_token=HF_TOKEN)

# Test questions
test_questions = [
    "Calculate the derivative of the function f(x) = 3x² + 5x - 2 using the power rule.",
    "Determine the value of x in the equation 3x + 7 = 22 by performing inverse operations.",
    "The photosynthetic process converts light energy into chemical energy through complex reactions.",
]

# Simplify each question
results = []
for question in test_questions:
    result = simplifier.simplify(
        original_text=question,
        simplification_level="moderate",
        preserve_math=True
    )
    results.append(result)
    
    print(f"{'='*80}")
    print(f"ORIGINAL: {question}")
    print(f"SIMPLIFIED: {result['simplified_text']}")
    print(f"STATUS: {'✅ PASSED' if result['success'] else '⚠️ FLAGGED'}")
    print(f"Semantic: {result['semantic_score']:.3f} | Difficulty Change: {result['difficulty_change']:.1f}%")
    print(f"{'='*80}\n")

# Summary statistics
successful = sum(1 for r in results if r['success'])
avg_semantic = sum(r['semantic_score'] for r in results) / len(results)
avg_difficulty = sum(r['difficulty_change'] for r in results) / len(results)

print(f"\n✅ SUCCESS RATE: {successful}/{len(results)} ({successful/len(results)*100:.1f}%)")
print(f"📊 Average Semantic Similarity: {avg_semantic:.3f}")
print(f"📊 Average Difficulty Change: {avg_difficulty:.1f}%")
