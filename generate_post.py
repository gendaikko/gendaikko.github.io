from google import genai
import datetime
import os

# APIキー設定
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 今日の日付
date_str = datetime.datetime.now().strftime("%Y-%m-%d")

# プロンプト（Hugo形式）
prompt = f"""
今日は{date_str}です。
以下のHugo用Front Matterを含む、SEOに強い日本語のブログ記事を1つ作成してください。

---
title: "AIが自動生成した今日のニュース"
date: {date_str}
draft: false
---

# 記事のタイトル
（ここに見出し3つ以上、1500文字程度の本文を作成）
"""

# 生成（ログのリストにあった 'gemini-2.0-flash' を指定）
try:
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )

    # フォルダ作成
    os.makedirs("content/posts", exist_ok=True)

    # 保存
    filename = f"content/posts/{date_str}-auto-post.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"成功: 記事を生成しました ({filename})")

except Exception as e:
    print(f"エラーが発生しました: {e}")
    raise
