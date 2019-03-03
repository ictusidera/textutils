# ictusidera/textutils

https://github.com/ictusidera/textutils.git

## textutils.py
テキスト操作ユーティリティコマンド

# Usage: 
```cmd
  textutils.py COMMAND [ARGS] [OPTIONS]...
```

### Options:

  --help : ヘルプメッセージを表示します。  
  --file / -f : ファイル名を指定します。テキスト形式のファイル(*.txt/*.csvなど)のみが指定できます。指定したコマンドの入力を指定したファイルから行うことができます。  
  --text / -t : コマンドへ入力する文字列を指定します。　example) textutils -t "ABCDEF"  

### Other:
  
  一部のコマンドでは入力を標準入力から取ることができます。  
  一部のコマンドとは以下の通りです。
  
    to-csv, space-to-tab, tab-to-space, reverse, line-sort, line-sort-smart
  
  標準入力から入力を取ると、unixライクなパイプチェーンが実現できます。  
  一例を示します。

  ```cmd
  # タブ区切り(Excelからコピペしたテキスト)のファイルをCSV形式に変換し、一列目(数字)の昇順に並び替えるサンプル

  textutils to-csv < text.txt | textutils line-sort > out.txt
  ```

### Commands:

  #### combinations 組み合わせを生成します 
    exp(expressions): 出力するテキストのフォーマットを指定します。  ex) "{0}-{1}"
    population: 母集合を指定します。 ex) "ABCDE"
    count: 組み合わせの数を指定します。(populationからcount個数選ぶ組み合わせを出力)

    example) textutils combinations {0}-{1} A B C 2 -> A-B, A-C, B-C 

  #### line-sort        行の並べ替え(文字列ABCD順, 数字を数字として並べ替え) 
    example) textutils line-sort -f file_name.txt > out.txt
    
    入力:[file_name.txt]\n
        10 テスト結果A\n
        9 テスト結果B\n
        11 テスト結果C\n
        1 テスト結果D\n
        EF\n
        AB\n
        CD\n
        GH\n
    
    出力:[out.txt]\n
        1 テスト結果D\n
        10 テスト結果A\n
        11 テスト結果C\n
        9 テスト結果B\n
        AB\n
        CD\n
        EF\n
        GH\n

  #### line-sort-smart  賢い行並べ替え(数字を数値として並べ替え) 
    example) textutils line-sort-smart -f file_name.txt > out.txt
    
    入力:[file_name.txt]\n
        10 テスト結果A\n
        9 テスト結果B\n
        11 テスト結果C\n
        1 テスト結果D\n
    
    出力:[out.txt]\n
        1 テスト結果D\n
        9 テスト結果B\n
        10 テスト結果A\n
        11 テスト結果C\n

  #### product          デカルト積を生成します
    exp(expressions): 出力するテキストのフォーマットを指定します。 ex) "{0}-{1}"
    first: 1つ目の集合
    second: 2つ目の集合

    example) textutils product {0}-{1} AB CD -> AB, AC, AD, BC, BD

  #### reverse 文字列を逆順にして返します 
    example) textutils reverse -t 0123456 -> 6543210

    -f/file : テキストファイルを指定すると、中身を読み込み変換して出力します。
        textutils reverse -f filename.txt > out.txt """
        
  #### space-to-tab スペースをタブ文字に置換します。(連続する空白文字を一つのタブに置き換え) 
    example) textutils space-to-tab -t 1 2 3 -> 1\t2\t3

    -f/file : テキストファイルを指定すると、ファイルを読み込み変換して出力します。
        textutils space_to_tab　-f filename.txt > out.txt

  #### tab-to-space タブ文字をスペースに置換します。(連続するタブ文字を一つのスペースに置き換え) 
    example) textutils tab-to-space -t 1\t2\t3 -> 1 2 3

    -f/file : テキストファイルを指定すると、ファイルを読み込み変換して出力します。
        textutils tab_to_space -f filename.txt > out.txt

  #### to-csv スペースをカンマに置換します(連続する空白文字を一つのカンマに置き換え) 
    example) textutils to-csv -t 1 2 3 -> 1,2,3

    -f/file : テキストファイルを指定すると、中身を読み込み変換して出力します。
        textutils to-csv -f filename.txt > out.txt


# Author:
ictusidera@gmail.com

# Licence: 
This software is released under the MIT License, see LICENSE.

