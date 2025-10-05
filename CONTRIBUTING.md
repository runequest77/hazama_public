# 貢献ガイド

hazama_publicリポジトリへの貢献に興味を持っていただき、ありがとうございます。

## 貢献の流れ

### 1. リポジトリのフォーク（初回のみ）

GitHubでこのリポジトリをフォークします。

### 2. リポジトリのクローン

```bash
git clone https://github.com/あなたのユーザー名/hazama_public.git
cd hazama_public
```

### 3. ブランチの作成

```bash
git checkout -b feature/記事名または変更内容
```

ブランチ名の例：
- `feature/new-article-game-system`
- `feature/update-character-guide`
- `fix/typo-in-readme`

### 4. 記事の作成・編集

#### Wiki構文の記事を作成する場合

`articles/wiki/` ディレクトリに `.txt` ファイルを作成します。

```bash
cp templates/wiki_template.txt articles/wiki/your-article-name.txt
```

#### Markdownの記事を作成する場合

`articles/markdown/` ディレクトリに `.md` ファイルを作成します。

```bash
cp templates/markdown_template.md articles/markdown/your-article-name.md
```

### 5. 変更のコミット

```bash
git add .
git commit -m "記事追加: 〇〇について"
```

コミットメッセージの例：
- `記事追加: ゲームシステムガイド`
- `記事更新: キャラクター一覧に新キャラクターを追加`
- `修正: タイポの修正`
- `ドキュメント: README.mdの改善`

### 6. リモートリポジトリへのプッシュ

```bash
git push origin feature/記事名または変更内容
```

### 7. プルリクエストの作成

GitHubでプルリクエストを作成します。

プルリクエストには以下を含めてください：
- 変更内容の説明
- 追加・編集した記事の概要
- 関連するissue番号（あれば）

## 記事作成のガイドライン

### ファイル命名規則

- **Wiki構文**: `articles/wiki/記事名.txt`
- **Markdown**: `articles/markdown/記事名.md`
- ファイル名は英数字とハイフンを使用（日本語は避ける）
- 小文字を推奨
- 例: `character-guide.txt`, `game-system.md`

### 記事の内容

1. **タイトルを明確に**
   - 記事の内容が一目で分かるタイトルをつける

2. **概要を書く**
   - 記事の冒頭に概要を記載する
   - 読者が記事の内容を素早く理解できるようにする

3. **適切な見出しを使用**
   - 内容を構造化し、読みやすくする
   - 階層を適切に使い分ける

4. **正確な情報を記載**
   - 誤った情報や推測を避ける
   - 情報源がある場合は明記する

5. **公序良俗に反しない**
   - 不適切な内容は含めない
   - 他者の権利を侵害しない

### 記法の選択

- **Wiki構文**: hazama wikiに直接投稿する予定の記事
- **Markdown**: 一般的な文書として管理したい記事、またはGitHub上で読みやすくしたい記事

## レビュープロセス

1. プルリクエストが作成されると、メンテナーがレビューします
2. 必要に応じて修正を依頼される場合があります
3. レビューが完了し、承認されるとマージされます

## 質問やサポート

- Issuesで質問や提案ができます
- バグや改善提案も歓迎します

## 行動規範

- 敬意を持ったコミュニケーションを心がけてください
- 建設的なフィードバックを提供してください
- 多様性と包摂性を尊重してください

## ライセンス

このリポジトリに貢献することで、あなたの貢献が[プロジェクトのライセンス]の下で公開されることに同意したものとみなされます。

## 参考資料

- [Wiki構文ガイド](docs/wiki_syntax_guide.md)
- [Markdownガイド](docs/markdown_guide.md)
- [hazama wiki](https://w.atwiki.jp/hazama/)

---

貢献していただき、ありがとうございます！
