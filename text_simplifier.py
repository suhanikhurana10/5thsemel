from huggingface_hub import InferenceClient
from semantic_checker import SemanticChecker
from difficulty_scorer import DifficultyScorer
from prompts import SimplificationPrompts

class TextSimplifier:
    """Main text simplification engine with validation and adaptive regeneration."""
    
    def __init__(self, hf_token: str):
        """
        Initialize the text simplifier.
        
        Args:
            hf_token: Hugging Face API token
        """
        self.semantic_checker = SemanticChecker()
        self.difficulty_scorer = DifficultyScorer()
        self.prompts = SimplificationPrompts()
        
        self.client = InferenceClient(token=hf_token)
        
        # Validation thresholds
        self.semantic_threshold = 0.85
        self.difficulty_threshold = 10.0  # max % change
        self.max_attempts = 3
    
    def simplify(self, original_text, simplification_level="moderate", preserve_math=True):
        """
        Simplify text with validation and adaptive regeneration.
        
        Args:
            original_text: Original assessment question
            simplification_level: "minimal", "moderate", or "significant"
            preserve_math: Whether to keep math notation intact
            
        Returns:
            dict with keys:
                - success: bool
                - simplified_text: str
                - semantic_score: float
                - difficulty_change: float
                - attempt: int
                - flagged: bool (True if failed validation)
        """
        print(f"\n{'='*80}")
        print(f"SIMPLIFYING: {original_text[:60]}...")
        print(f"{'='*80}\n")
        
        original_difficulty = self.difficulty_scorer.calculate_difficulty(original_text)
        orig_score = original_difficulty["composite_difficulty"]
        
        best_result = None
        best_overall_score = 0
        
        for attempt in range(1, self.max_attempts + 1):
            print(f"🔄 Attempt {attempt}/{self.max_attempts}")
            
            # Generate simplified version
            simplified = self._call_llm(original_text, simplification_level, preserve_math, attempt)
            
            if not simplified:
                print("  ❌ Generation failed")
                continue
            
            # Validate semantic similarity
            semantic_score = self.semantic_checker.check_similarity(original_text, simplified)
            semantic_pass = semantic_score >= self.semantic_threshold
            
            # Validate difficulty alignment
            simp_difficulty = self.difficulty_scorer.calculate_difficulty(simplified)
            simp_score = simp_difficulty["composite_difficulty"]
            difficulty_change = abs(simp_score - orig_score) / orig_score * 100 if orig_score > 0 else 0
            difficulty_pass = difficulty_change <= self.difficulty_threshold
            
            # Calculate overall quality score
            overall_score = (semantic_score * 0.7) + ((100 - min(difficulty_change, 100)) / 100 * 0.3)
            
            print(f"  📊 Semantic: {semantic_score:.3f} {'✓' if semantic_pass else '✗'}")
            print(f"  📊 Difficulty: {difficulty_change:.1f}% change {'✓' if difficulty_pass else '✗'}")
            
            # Track best result
            if overall_score > best_overall_score:
                best_overall_score = overall_score
                best_result = {
                    "simplified_text": simplified,
                    "semantic_score": semantic_score,
                    "semantic_pass": semantic_pass,
                    "difficulty_change": difficulty_change,
                    "difficulty_pass": difficulty_pass,
                    "attempt": attempt,
                }
            
            # Check if all validations passed
            if semantic_pass and difficulty_pass:
                print(f"  ✅ All checks passed!\n")
                best_result["success"] = True
                best_result["flagged"] = False
                return best_result
            
            print(f"  ⚠️ Validation failed, trying again...\n")
        
        # Max attempts reached
        print(f"⚠️ Max attempts reached. Flagged for review\n")
        best_result["success"] = False
        best_result["flagged"] = True
        return best_result
    
    def _call_llm(self, original, level, preserve_math, attempt):
        """Call Hugging Face LLM API with adaptive temperature."""
        temperature = 0.3 + (attempt - 1) * 0.15
        prompt = self.prompts.get_simplification_prompt(original, level, preserve_math)
        
        messages = [{"role": "user", "content": prompt}]
        
        try:
            response = self.client.chat_completion(
                messages=messages,
                model="meta-llama/Llama-3.2-3B-Instruct",
                max_tokens=300,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"  ❌ Error: {e}")
            return None
