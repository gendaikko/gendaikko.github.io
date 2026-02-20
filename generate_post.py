import google.generativeai as genai
import datetime
import os

# API設定
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# 今日の日付
date_str = datetime.datetime.now().strftime("%Y-%m-%d")

# プロンプト
prompt = f"""
今日は{date_str}です。
SEOを意識した日本語ブログ記事を書いてください。
・Markdown形式
・1行目はタイトル（# 付き）
・見出しを3つ以上含める
・約1500文字
"""

# 生成
response = model.generate_content(prompt)

# content ディレクトリを作る
os.makedirs("content/posts", exist_ok=True)

# 保存
filename = f"content/posts/{date_str}-auto-post.md"
with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

print("記事を生成しました:", filename)
