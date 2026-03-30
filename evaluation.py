import time
from main import generate_answer  # your existing function

# -------------------------------
# ✅ Test Questions (8 total)
# -------------------------------
test_questions = [
    # Prereq (must answer + cite)
    ("What are prerequisites for database systems?", "prereq"),
    ("Can I take 6.5831 after 6.1210?", "prereq"),
    ("Do I need 6.1800 before database systems?", "prereq"),

    # Chain reasoning
    ("What path leads to database systems?", "chain"),

    # Program
    ("What are requirements for CS degree?", "program"),

    # NOT IN DOCS (must abstain)
    ("Is database systems offered in Fall?", "not_in_docs"),
    ("Who teaches database systems?", "not_in_docs"),
]

# -------------------------------
# ✅ Retry wrapper (handles 429)
# -------------------------------
def safe_generate(query, retries=3):
    for i in range(retries):
        try:
            return generate_answer(query)
        except Exception as e:
            print(f"⚠️ Retry {i+1} due to error:", e)
            time.sleep(60)  # wait for quota reset
    return "ERROR: Failed after retries"

# -------------------------------
# ✅ Evaluation Metrics
# -------------------------------
def has_citation(answer):
    return "[Source:" in answer

def is_abstained(answer):
    return "I don't have that information" in answer

# -------------------------------
# 🚀 Run Evaluation
# -------------------------------
print("🚀 Running Evaluation...\n")

total = len(test_questions)
citation_count = 0
abstain_correct = 0
abstain_total = 0

for i, q in enumerate(test_questions):
    print(f"\n--- Q{i+1} ({q['type']}) ---")
    print("Question:", q["question"])

    answer = safe_generate(q["question"])
    print("Answer:\n", answer)

    # ✅ Citation check
    if has_citation(answer):
        citation_count += 1

    # ✅ Abstention check
    if q["type"] == "not_in_docs":
        abstain_total += 1
        if is_abstained(answer):
            abstain_correct += 1

    # ✅ Avoid rate limit (IMPORTANT)
    time.sleep(15)

# -------------------------------
# 📊 Final Results
# -------------------------------
print("\n📊 FINAL RESULTS")
print(f"Total Questions: {total}")
print(f"Citation Coverage: {(citation_count / total) * 100:.2f}%")

if abstain_total > 0:
    print(f"Abstention Accuracy: {(abstain_correct / abstain_total) * 100:.2f}%")
else:
    print("No abstention questions found.")