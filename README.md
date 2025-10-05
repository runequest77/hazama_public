# hazama_public

## 概要

このリポジトリは [hazama wiki](https://w.atwiki.jp/hazama/) 用の公開記事を編集・管理するためのリポジトリです。

## 使用する記法

- Wiki構文（@wikiの構文）
- Markdown

## ディレクトリ構造

```
.
├── README.md           # このファイル
├── articles/          # 記事ファイル
│   ├── wiki/         # Wiki構文で書かれた記事
│   └── markdown/     # Markdownで書かれた記事
├── templates/         # 記事のテンプレート
└── docs/             # ドキュメント
```

## 記事の作成方法

### Wiki構文の記事

`articles/wiki/` ディレクトリに `.txt` ファイルを作成してください。

テンプレート: `templates/wiki_template.txt` を参照

### Markdownの記事

`articles/markdown/` ディレクトリに `.md` ファイルを作成してください。

テンプレート: `templates/markdown_template.md` を参照

## 編集ワークフロー

1. このリポジトリをクローン
2. 新しいブランチを作成
3. 記事を作成・編集
4. コミット・プッシュ
5. プルリクエストを作成

## 貢献ガイドライン

- 記事は日本語で書いてください
- ファイル名は内容を表す分かりやすい名前にしてください
- コミットメッセージは変更内容を明確に記述してください
- 記事の内容は公序良俗に反しないようにしてください

## 参考リンク

- [hazama wiki](https://w.atwiki.jp/hazama/)
- [@wiki 構文ガイド](https://www1.atwiki.jp/guide/pages/468.html)