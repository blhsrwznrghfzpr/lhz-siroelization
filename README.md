#lhz-siroelization

「LHZシロエ化」は、セルデシア・ガゼットの情報を再編集して
項目ごとに分類するツールです。

##実行に必要なもの
###Python
Pythonの実行環境が必要です。LinuxやMacならば標準のPythonが使えます。Windowsの場合は、CPythonかIronPythonを使うと良いでしょう。

Python for Windows
https://www.python.org/downloads/windows/

IronPython
https://ironpython.codeplex.com/


###PyPDF2
PDFの操作のためにPyPDF2が必要です。

easy_install を使えば楽にインストールできます。

```$ sudo easy_install pypdf2```

PyPDF2
https://github.com/mstamy2/PyPDF2


###PDF本体
下記のURLから、セルデシア・ガゼットをダウンロードして、含まれるPDFファイルを取り出してください。

セルデシア・ガゼット
http://lhrpg.com/lhz/download

```source``` ディレクトリにPDFファイルを置いてください。

```
$ ls  source/
CeldesiaG01.pdf
CeldesiaG02.pdf
CeldesiaG03.pdf
CeldesiaG04.pdf
CeldesiaG05.pdf
CeldesiaG06.pdf
CeldesiaG07.pdf
```

##使い方
```$ ./lhz-siroelization.py```

実行したディレクトリに、PDFファイルができているはずです。

- scenario.pdf (シナリオ)
- rules.pdf (ルール・解説)
- culture.pdf (ヤマト風土記)
- d66.pdf (できるかな66)
- hotlog.pdf (コッペリア・ホットログ)
- soudan.pdf (ログホラ相談窓口)

##リポジトリ
silver-rain/lhz-siroelization
https://github.com/silver-rain/lhz-siroelization


