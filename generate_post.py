from google import genai [cite: 5]
import datetime [cite: 5]
import os [cite: 5]

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"]) [cite: 5]
date_str = datetime.datetime.now().strftime("%Y-%m-%d") [cite: 5]

# Hugoで表示するためにタイトルや日付の情報を追加
prompt = f"""
今日は{date_str}です。
SEOを意識した日本語ブログ記事を、以下のHugo形式で書いてください。

---
title: "記事のタイトル"
date: {date_str}
draft: false
---

# 記事のタイトル
（ここに見出し3つ以上、1500文字程度の本文）
"""

# モデル名を 'gemini-1.5-pro' に修正（models/ は不要） 
response = client.models.generate_content(
    model="gemini-1.5-pro", 
    contents=prompt
)

os.makedirs("content/posts", exist_ok=True) [cite: 5]
filename = f"content/posts/{date_str}-auto-post.md" [cite: 5]

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text) [cite: 5]

print("記事を生成しました:", filename) [cite: 5]
