import language_tool_python
from textblob import TextBlob
import textstat

# Step 1: Student submits the assignment
def submit_assignment():
    print("=== Step 1: Student Submission ===")
    text = input("\nPaste your assignment below:\n")
    return text

# Step 2: Instructor reviews content
def instructor_review(text):
    print("\n=== Step 2: Instructor Review ===")
    print("Assignment received. Starting automated NLP analysis...\n")

# Step 3: Define feedback criteria
def analyze_text(text):
    print("=== Step 3 & 4: Feedback Criteria & Feedback ===")
    tool = language_tool_python.LanguageTool('en-US')
    blob = TextBlob(text)
    
    feedback = []

    # Grammar check
    matches = tool.check(text)
    if matches:
        feedback.append(f"⚠️ Found {len(matches)} grammar/style issues. Example: '{matches[0].message}'")
    else:
        feedback.append("✅ No grammar/style issues found.")

    # Spelling check
    misspelled = [(word, word.correct()) for word in blob.words if word.lower() != word.correct().lower()]
    if misspelled:
        example = misspelled[0]
        feedback.append(f"🔠 Spelling issue: '{example[0]}' → '{example[1]}'")
    else:
        feedback.append("✅ No spelling issues detected.")

    # Readability
    flesch = textstat.flesch_reading_ease(text)
    grade = textstat.flesch_kincaid_grade(text)
    feedback.append(f"📊 Readability Score: {flesch:.2f}, Grade Level: {grade:.2f}")
    if flesch < 50:
        feedback.append("💡 Suggestion: Simplify sentence structure to improve clarity.")

    # Sentiment
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    feedback.append(f"💬 Sentiment: Polarity={polarity:.2f}, Subjectivity={subjectivity:.2f}")
    if subjectivity > 0.6:
        feedback.append("💡 Suggestion: Use more objective language for academic tone.")
    
    return feedback

# Step 5: Student reflects on feedback
def reflect_on_feedback(feedback):
    print("\n=== Step 5: Student Reflects on Feedback ===")
    for point in feedback:
        print(point)
    print("\nPlease revise your assignment based on the above feedback.\n")

# Step 6: Student revises assignment
def revise_assignment():
    print("=== Step 6: Student Resubmission ===")
    revised_text = input("\nPaste your revised assignment below:\n")
    return revised_text

# Main Workflow
def main():
    original = submit_assignment()
    instructor_review(original)
    feedback = analyze_text(original)
    reflect_on_feedback(feedback)
    revised = revise_assignment()

    print("\nRe-analyzing revised submission...\n")
    revised_feedback = analyze_text(revised)
    
    print("\n=== Final Feedback on Revised Submission ===")
    for point in revised_feedback:
        print(point)

if __name__ == "__main__":
    main()
