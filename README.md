# copier example

Python製のボイラープレートツールCopierのサンプルです。

サンプル記載の記事 -> 公開されたら載せます

## 使い方

このリポジトリをダウンロードしてください。zipダウンロードがオススメです。

my_template内部で`git clone` を利用した時に サブモジュール的な扱いになり学ぶ際に混乱する可能性があります。

### コマンドラインツールから使う

* `pip install copier` でCopierをインストールする
  * もしくは、pipxを使ってコマンドラインツールとして用意することも可能
* `copier copy <テンプレートのパス> <出力先のパス>` でプロジェクトを作成する
  * `copier_exam % copier copy ./my_template ./generated_project`

### Pythonから使う

* `pip install copier` でCopierをインストールする
* `copier.copy()` を実行する
  * `copier.copy('./my_template', './generated_project')`
  * サンプルコード -> [copier_exam.py](./copier_exam.py)
