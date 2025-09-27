# Sandbox

## 概要

いろいろと気になったことを試してみるための雑多なコード置き場。

## ディレクトリ・ファイル構成

```text
+ .github/
  + workflows/
    + cmake_001.yml   : cmake/001 のビルド用 workflow 定義
    + cmake_002.yml   : cmake/002 のビルド用 workflow 定義
    + cmake_003.yml   : cmake/003 のビルド用 workflow 定義
    + python_001.yml  : python/001 の実行用 workflow 定義
+ projects/
  + cmake/            : CMake練習環境
    + 001/
      + README.md     : この環境 (cmake/001) の説明
      + ...
    + ...
  + python/           : Python練習環境
    + 001/
    + ...
```

個々の環境についての説明は、個別のディレクトリ以下の `README.md` を参照。
