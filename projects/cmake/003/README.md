# cmake/003

## 概要

ライブラリを生成し、.c にリンクして実行ファイルを生成する。
ただし、ライブラリも複数のコンポーネントから構成されている。

## ディレクトリ・ファイル構成

```text
+ 003/
  + LibA/               : ライブラリディレクトリ
    + CompAdd/
      + CMakeLists.txt  : コンポーネントをビルドするための CMakeLists.txt
      + add.c
      + add.h
    + CompSub/
      + CMakeLists.txt  : コンポーネントをビルドするための CMakeLists.txt
      + sub.c
      + sub.h
    + CMakeLists.txt    : ライブラリをビルドするための CMakeLists.txt
    + liba.c
    + liba.h            : ライブラリが外部に公開する I/F 定義
  + CMakeLists.txt      : 全体ビルドのための CMakeLists.txt
  + main.c              : メイン関数
```
