# cmake/002

## 概要

ライブラリを生成し、.c にリンクして実行ファイルを生成する。

## ディレクトリ・ファイル構成

```text
+ 002/
  + LibA/             : ライブラリディレクトリ
    + include/
      + liba.h        : ライブラリが外部に開示している I/F 定義
    + source/
      + liba.c        : ライブラリの実装
    + CMakeLists.txt  : ライブラリをビルドするための CMakeLists.txt
  + CMakeLists.txt    : 全体ビルドのための CMakeLists.txt
  + main.c            : メイン関数
```
