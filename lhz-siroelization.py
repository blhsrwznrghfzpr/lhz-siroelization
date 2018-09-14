#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2015, SilverRain.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
# * The name of the author may not be used to endorse or promote products
# derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from PyPDF2 import PdfFileMerger
import os
import os.path
import zipfile
import urllib2
import shutil

# ページ数は全てページ内の表記。実際のページは+1
# シナリオ
scenario = [("CeldesiaG01.pdf", 2, 31),
            ("CeldesiaG02.pdf", 2, 27),
            ("CeldesiaG03.pdf", 2, 19),
            ("CeldesiaG07.pdf", 2, 62),
            ("CeldesiaG12.pdf", 9, 24)]

# ルール・解説類
rules = [("CeldesiaG03.pdf", 20, 32),
         ("CeldesiaG04.pdf", 26, 31),
         ("CeldesiaG05.pdf", 10, 15),
         ("CeldesiaG06.pdf", 2, 14),
         ("CeldesiaG08.pdf", 2, 6),
         ("CeldesiaG09.pdf", 2, 13),
         ("CeldesiaG12.pdf", 2, 8)]


# ヤマト風土記
culture = [("CeldesiaG01.pdf", 34, 36),
           ("CeldesiaG02.pdf", 39, 41),
           ("CeldesiaG03.pdf", 35, 37),
           ("CeldesiaG04.pdf", 32, 34),
           ("CeldesiaG05.pdf", 18, 20),
           ("CeldesiaG06.pdf", 15, 17),
           ("CeldesiaG07.pdf", 63, 65),
           ("CeldesiaG08.pdf", 7, 9),
           ("CeldesiaG09.pdf", 14, 16),
           ("CeldesiaG10.pdf", 2, 7),
           ("CeldesiaG11.pdf", 27, 29),
           ("CeldesiaG12.pdf", 25, 27),
           ("CeldesiaG13.pdf", 2, 4),
           ("CeldesiaG14.pdf", 7, 10),
           ("CeldesiaG15.pdf", 2, 4)]


# 列島生物図鑑
encyclopedia = [("CeldesiaG01.pdf", 38, 41),
                ("CeldesiaG02.pdf", 28, 36),
                ("CeldesiaG03.pdf", 39, 42),
                ("CeldesiaG04.pdf", 35, 39),
                ("CeldesiaG05.pdf", 21, 25),
                ("CeldesiaG06.pdf", 18, 28),
                ("CeldesiaG07.pdf", 66, 70),
                ("CeldesiaG08.pdf", 10, 12),
                ("CeldesiaG09.pdf", 17, 23),
                ("CeldesiaG10.pdf", 8, 14),
                ("CeldesiaG11.pdf", 30, 34),
                ("CeldesiaG12.pdf", 28, 33),
                ("CeldesiaG13.pdf", 5, 13),
                ("CeldesiaG14.pdf", 10, 14),
                ("CeldesiaG15.pdf", 5, 10)]

# できるかな66
d66 = [("CeldesiaG01.pdf", 42, 42),
       ("CeldesiaG02.pdf", 43, 43),
       ("CeldesiaG03.pdf", 43, 43),
       ("CeldesiaG04.pdf", 40, 41),
       ("CeldesiaG05.pdf", 26, 27),
       ("CeldesiaG06.pdf", 29, 30),
       ("CeldesiaG07.pdf", 71, 71),
       ("CeldesiaG08.pdf", 13, 13),
       ("CeldesiaG09.pdf", 22, 22),
       ("CeldesiaG10.pdf", 15, 17),
       ("CeldesiaG11.pdf", 35, 35),
       ("CeldesiaG12.pdf", 34, 40),
       ("CeldesiaG13.pdf", 14, 21),
       ("CeldesiaG14.pdf", 15, 17),
       ("CeldesiaG15.pdf", 10, 12)]


# コッペリア・ホットログ
hotlog = [("CeldesiaG01.pdf", 44, 44),
          ("CeldesiaG02.pdf", 45, 45),
          ("CeldesiaG03.pdf", 45, 45),
          ("CeldesiaG05.pdf", 29, 29),
          ("CeldesiaG07.pdf", 73, 73),
          ("CeldesiaG08.pdf", 16, 16),
          ("CeldesiaG09.pdf", 25, 25),
          ("CeldesiaG11.pdf", 39, 39)]


# ログホラ相談窓口
soudan = [("CeldesiaG01.pdf", 45, 45),
          ("CeldesiaG02.pdf", 46, 46),
          ("CeldesiaG03.pdf", 46, 46),
          ("CeldesiaG04.pdf", 43, 43),
          ("CeldesiaG05.pdf", 30, 30),
          ("CeldesiaG06.pdf", 35, 35),
          ("CeldesiaG07.pdf", 74, 74),
          ("CeldesiaG08.pdf", 17, 17),
          ("CeldesiaG09.pdf", 26, 26),
          ("CeldesiaG10.pdf", 20, 20),
          ("CeldesiaG11.pdf", 40, 40),
          ("CeldesiaG12.pdf", 43, 43),
          ("CeldesiaG13.pdf", 24, 24),
          ("CeldesiaG14.pdf", 19, 19),
          ("CeldesiaG15.pdf", 15, 15)]


# ファイル名とデータの組
output_structure = [('lhz-scenario.pdf', scenario),
                    ('lhz-rules.pdf', rules),
                    ('lhz-culture.pdf', culture),
                    ('lhz-d66.pdf', d66),
                    ('lhz-hotlog.pdf', hotlog),
                    ('lhz-soudan.pdf', soudan)]

# 元のファイル
# ウェンズデイなども流用できるよう、冗長にしています
download_source = {"CeldesiaG01.pdf": ("CeldesiaG01.zip", "http://lhrpg.com/data/CeldesiaG01.zip"),
                   "CeldesiaG02.pdf": ("CeldesiaG02.zip", "http://lhrpg.com/data/CeldesiaG02.zip"),
                   "CeldesiaG03.pdf": ("CeldesiaG03.zip", "http://lhrpg.com/data/CeldesiaG03.zip"),
                   "CeldesiaG04.pdf": ("CeldesiaG04.zip", "http://lhrpg.com/data/CeldesiaG04.zip"),
                   "CeldesiaG05.pdf": ("CeldesiaG05.zip", "http://lhrpg.com/data/CeldesiaG05.zip"),
                   "CeldesiaG06.pdf": ("CeldesiaG06.zip", "http://lhrpg.com/data/CeldesiaG06.zip"),
                   "CeldesiaG07.pdf": ("CeldesiaG07.zip", "http://lhrpg.com/data/CeldesiaG07.zip"),
                   "CeldesiaG08.pdf": ("CeldesiaG08.zip", "http://lhrpg.com/data/CeldesiaG08.zip"),
                   "CeldesiaG09.pdf": ("CeldesiaG09.zip", "http://lhrpg.com/data/CeldesiaG09.zip"),
                   "CeldesiaG10.pdf": ("CeldesiaG10.zip", "http://lhrpg.com/data/CeldesiaG10.zip"),
                   "CeldesiaG11.pdf": ("CeldesiaG11.zip", "http://lhrpg.com/data/CeldesiaG11.zip"),
                   "CeldesiaG12.pdf": ("CeldesiaG12.zip", "http://lhrpg.com/data/CeldesiaG12.zip"),
                   "CeldesiaG13.pdf": ("CeldesiaG13.zip", "http://lhrpg.com/data/CeldesiaG13.zip"),
                   "CeldesiaG14.pdf": ("CeldesiaG14.zip", "http://lhrpg.com/data/CeldesiaG14.zip"),
                   "CeldesiaG15.pdf": ("CeldesiaG15.zip", "http://lhrpg.com/data/CeldesiaG15.zip")}

def make_pdf(output, container):
    u'''PDFを指定に従い作成する'''
    # マージするためのオブジェクト
    merger = PdfFileMerger()
    print("{} making...".format(output))

    # マージするファイルを登録
    for item in container:
        datafile, start, end = item
        # ZIPファイルの拡張子抜き
        basename = os.path.splitext(download_source[datafile][0])[0]
        # どちらかが正しい(ディレクトリつきZIPとそうでないのがある)
        source_with_dir = os.path.join('source', basename, datafile)
        source_without_dir = os.path.join('source', datafile)
        
        # どちらが正しいか判定
        if  os.access(source_with_dir, os.R_OK):
            source = source_with_dir
        else:
            source = source_without_dir

        # zipファイルの中のファイルを直接開く
        with open(source, 'rb') as inputpdf:
            # 表示ページ数と実ページ数の整合のために1ページ増量だが、0スタートで補正できている
            merger.append(inputpdf, pages = (start, end + 1))

    # マージの実行
    with open(output, 'wb') as outputpdf:
        merger.write(outputpdf)

def do_download(outputdir, filename, url):
    u'''URLからファイルをダウンロードする'''
    # ダウンロードのバッファサイズ
    bufsize = 1024 * 1024
    # 出力ファイルのパス名つき情報
    output_pathname = os.path.join(outputdir, filename)
    
    # ファイルが存在したならば、ダウンロードは行なわない
    if os.access(output_pathname, os.R_OK):
        print("{} is skipped".format(filename))
        return True
    else:
        print("{} downloading...".format(filename))    

    # URLをオープンして、中身をファイルにコピーする
    urlhandle = urllib2.urlopen(url)
    with open(output_pathname, 'wb') as filehandle:
        shutil.copyfileobj(urlhandle, filehandle, bufsize)
    urlhandle.close()

def do_unzip(outputdir, filename):
    u'''UNZIP'''
    print("{} extracting...".format(filename))    
    # 出力ファイルのパス名つき情報
    output_pathname = os.path.join(outputdir, filename)
    # ZIPファイルを展開する
    with zipfile.ZipFile(output_pathname, 'r') as zip:
        zip.extractall(outputdir)
        
# ファイルをsourceディレクトリにダウンロードする
for filename, data in download_source.items():
    zipname, download_url = data
    do_download("source", zipname, download_url)
    do_unzip("source", zipname)

# 構成物ごとに、pDFを作成
for item in output_structure:
    outputfile, data = item
    make_pdf(outputfile, data)
