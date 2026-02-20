from google import genai
import datetime
import os

# APIキー設定（GitHub Secretsから取得）
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 今日の日付を取得
date_str = datetime.datetime.now().strftime("%Y-%m-%d")

# プロンプトの作成
prompt = f"""
今日は{date_str}です。
以下のHugo用Front Matterを含む、SEOに強い日本語のブログ記事を作成してください。

---
title: "AIが自動生成した今日のニュース"
date: {date_str}
draft: false
---

# 記事のタイトル
（ここに見出し3つ以上、1500文字程度の本文を作成）
"""

# 生成（エラーを避けるため、軽量な1.5-flashを使用）
try:
    response = client.models.generate_content(
        model="gemini-1.5-flash", 
        contents=prompt
    )

    # 保存用フォルダの作成
    os.makedirs("content/posts", exist_ok=True)

    # 記事をファイルに保存
    filename = f"content/posts/{date_str}-auto-post.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"成功: 記事を生成しました ({filename})")

except Exception as e:
    print(f"エラーが発生しました: {e}")
    # 利用可能なモデルをログに出力して原因を探る
    print("利用可能なモデルのリストを確認中...")
    for m in client.models.list():
        print(f"使えるモデル名: {m.name}")
    raise
