from google import genai
import datetime
import os

# APIキー設定
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 今日の日付
date_str = datetime.datetime.now().strftime("%Y-%m-%d")

# プロンプト（Hugo形式を厳守）
prompt = f"""
今日は{date_str}です。
以下のHugo用Front Matterを含む、日本語のブログ記事を1つ作成してください。

---
title: "AIが見た{date_str}の世界"
date: {date_str}
draft: false
---

（ここから本文を開始してください。見出しを3つ以上使い、1500文字程度で詳しく書いてください）
"""

try:
    # ログで確認済み、かつ高性能な2.0-flashを使用
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=prompt
    )

    # 記事保存用フォルダ作成
    os.makedirs("content/posts", exist_ok=True)

    # 保存（ファイル名に日付を入れる）
    filename = f"content/posts/{date_str}-auto-post.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"成功: 記事を生成しました -> {filename}")

except Exception as e:
    print(f"エラー発生: {e}")
    raise
