from google import genai
import datetime
import os

# APIキー設定
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 日付
date_str = datetime.datetime.now().strftime("%Y-%m-%d")

# プロンプト（HugoのFront Matterを含めるように指示）
prompt = f"""
今日は{date_str}です。
SEOを意識した日本語ブログ記事を書いてください。

以下の形式で出力してください：
---
title: "記事のタイトル"
date: {date_str}
draft: false
---

# 記事のタイトル
（ここから本文。見出しを3つ以上含め、約1500文字で構成してください）
"""

# 生成 (モデル名の 'models/' を削除) [cite: 10]
response = client.models.generate_content(
    model="gemini-1.5-pro", 
    contents=prompt
)

# フォルダ作成
os.makedirs("content/posts", exist_ok=True)

# 保存
filename = f"content/posts/{date_str}-auto-post.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print("記事を生成しました:", filename)
