#lhz-siroelization

「LHZシロエ化」は、セルデシア・ガゼットの情報を再編集して
項目ごとに分類するツールです。

##実行に必要なもの
###Python
Pythonの実行環境が必要です。LinuxやMacならば標準のPythonが使えます。Windowsの場合は、公式のPythonのほうがモジュールがいれやすいのでおすすめです。慣れているならIronPythonでも良いでしょうが、手元では動作を確認していません。

Python for Windows
https://www.python.org/downloads/windows/


###PyPDF2
PDFの操作のためにPyPDF2が必要です。

PyPDF2
https://github.com/mstamy2/PyPDF2

easy_install を使えば楽にインストールできます。

LinuxかMacの場合は一発です。

```$ sudo easy_install pypdf2```

Windowsの場合は、Pythonの実行ファイルまでパスを通した上で、```Scripts``` ディレクトリにある easy_install.exe を実行する必要があります。

※Windows版の参考
http://bit.ly/1M7q2rl

```
>C:\Python27\Scripts\easy_install.exe pypdf2
Searching for pypdf2
Reading https://pypi.python.org/simple/pypdf2/
Reading http://github.com/mstamy2/PyPDF2/tarball/master
Reading http://mstamy2.github.com/PyPDF2
Best match: PyPDF2 1.24
Downloading https://pypi.python.org/packages/source/P/PyPDF2/PyPDF2-1.24.tar.gz#
md5=87cbb41c24bd98e6f70a37bb4a97446c
Processing PyPDF2-1.24.tar.gz
Writing c:\users\silver\appdata\local\temp\easy_install-fsgidv\PyPDF2-1.24\setup
.cfg
Running PyPDF2-1.24\setup.py -q bdist_egg --dist-dir c:\users\silver\appdata\loc
al\temp\easy_install-fsgidv\PyPDF2-1.24\egg-dist-tmp-opxi49
zip_safe flag not set; analyzing archive contents...
Moving pypdf2-1.24-py2.7.egg to c:\python27\lib\site-packages
Adding pypdf2 1.24 to easy-install.pth file

Installed c:\python27\lib\site-packages\pypdf2-1.24-py2.7.egg
Processing dependencies for pypdf2
Finished processing dependencies for pypdf2
```

###PDF本体
自動的にZIPファイルをダウンロードして展開しますので、インターネットに接続している必要があります。

セルデシア・ガゼット
http://lhrpg.com/lhz/download

```source``` ディレクトリにPDFファイルを置いてください。


##使い方
```$ ./lhz-siroelization.py```

実行したディレクトリに、PDFファイルができているはずです。

- lhz-index.pdf (目次一覧)
- lhz-scenario.pdf (シナリオ)
- lhz-rules.pdf (ルール・解説)
- lhz-culture.pdf (ヤマト風土記)
- lhz-d66.pdf (できるかな66)
- lhz-hotlog.pdf (コッペリア・ホットログ)
- lhz-teatime.pdf (エリッサのティータイム)
- lhz-soudan.pdf (ログホラ相談窓口)

##リポジトリ
silver-rain/lhz-siroelization
https://github.com/silver-rain/lhz-siroelization


