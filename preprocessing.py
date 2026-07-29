import pandas as pd
import re
text = """My dear friends, believe in yourself even when no one else does. Success is never achieved in a single day; it comes through hard work, patience, and dedication. Every failure is a lesson that makes you stronger and wiser. Never give up on your dreams because your determination will shape your future. Respect your parents, teachers, and everyone who supports your journey. Stay humble when you succeed and stay confident when you face difficulties. Use your knowledge and talents to make a positive difference in society. Keep learning, keep improving, and never stop chasing your goals. Your future is in your hands, so make every day count. Remember, with courage, discipline, and perseverance, nothing is impossible."""

df = pd.DataFrame({
    "Conversation": [text]
})
df.to_csv("raw.csv", index=False)

print("raw.csv created successfully!\n")
df = pd.read_csv("raw.csv")

print("Original Dataset\n")
print(df)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
df["Clean_Text"] = df["Conversation"].apply(clean_text)
df.to_csv("clean.csv", index=False)

print("\nPreprocessing Completed Successfully!")

print("\nClean Dataset\n")
print(df)
print("\nTotal Number of Conversations:", len(df))
print("Missing Conversations:", df["Conversation"].isnull().sum())
print("\nBefore and After Cleaning\n")

for i in range(len(df)):
    print("Original :")
    print(df.loc[i, "Conversation"])

    print("\nCleaned :")
    print(df.loc[i, "Clean_Text"])

    print("-" * 80)

