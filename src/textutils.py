# /usr/bin/env python
# -*- coding: utf-8 -*-

import click
import itertools

@click.group()
def command():
    u"""テキスト操作ユーティリティコマンド"""
    pass

@command.command()
@click.argument('exp', nargs=1)
@click.argument('population', nargs=-1)
@click.argument('count', nargs=1, type=int)
def combinations(exp, population, count,):
    u"""組み合わせを生成します\n
    exp(expressions): 出力するテキストのフォーマットを指定します。 ex) "{0}-{1}"
    population:       母集合を指定します。 ex) "ABCDE"
    count:            組み合わせの数を指定します。(populationからcount個数選ぶ組み合わせを出力)

    example) textutils combinations {0}-{1} A B C 2 -> A-B, A-C, B-C 
     """
    for item in itertools.combinations(population,count):
        print exp.format(*item)


@command.command()
@click.argument('exp', nargs=1)
@click.argument('first', nargs=1)
@click.argument('second', nargs=1)
def product(exp, first, second):
    u"""デカルト積を生成します\n
    exp(expressions): 出力するテキストのフォーマットを指定します。 ex) "{0}-{1}"
    first:            1つ目の集合
    second:           2つ目の集合

    example) textutils product {0}-{1} AB CD -> AB, AC, AD, BC, BD
    """

    for item in itertools.product(first,second):
        print exp.format(*item)

def smart_order(line):
    first = line.split()[:1]
    first = first[0].split(",")
    if first[0].isdigit():
        return int(first[0])
    else:
        return first[0]

@command.command()
@click.option('-f', '--file', type=click.File('r'), default=None)
def line_sort_smart(file):
    u"""賢い行並べ替え(数字を数値として並べ替え)\n
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
    """
    if(not (file)):
        lines = click.get_text_stream('stdin').readlines()
    else:
        with file as f:
            lines = f.readlines()
    for line  in sorted(lines,key=smart_order):
        click.echo(line, nl=False)

@command.command()
@click.option('-f', '--file', type=click.File('r'), default=None)
def line_sort(file):
    u"""行の並べ替え(文字列ABCD順, 数字を数字として並べ替え)\n
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
    """
    if(not (file)):
        lines = click.get_text_stream('stdin').readlines()
    else:
        with file as f:
            lines = f.readlines()

    for line  in sorted(lines):
        click.echo(line, nl=False)

@command.command()
@click.option('-f', '--file', type=click.File('r'), default=None)
@click.option('-t', '--text', default=None)
def csv_to_tab(file, text):
    u"""カンマ区切りをタブ区切りに置換します\n
    example) textutils csv-to-tab -t 1,2,3 -> 1\t2\t3

    -f/file : テキストファイルを指定すると、中身を読み込み変換して出力します。
        textutils csv-to-tab -f filename.txt > out.txt """
    if(not (file or text)):
        lines = click.get_text_stream('stdin').readlines()
    elif(file):
        with file as f:
            lines = f.readlines()
    elif(text):
        lines = [text]

    for line in lines:
        items = ['"' + x + '"' if "," in x else x for x in line.split(",")]
        click.echo(",".join(items))

@command.command()
@click.option('-f', '--file', type=click.File('r'), default=None)
@click.option('-t', '--text', default=None)
def to_csv(file, text):
    u"""スペースをカンマに置換します(連続する空白文字を一つのカンマに置き換え)\n
    example) textutils to-csv -t 1 2 3 -> 1,2,3

    -f/file : テキストファイルを指定すると、中身を読み込み変換して出力します。
        textutils to-csv -f filename.txt > out.txt """
    if(not (file or text)):
        lines = click.get_text_stream('stdin').readlines()
    elif(file):
        with file as f:
            lines = f.readlines()
    elif(text):
        lines = [text]

    for line in lines:
        items = ['"' + x + '"' if "," in x else x for x in line.split()]
        click.echo(",".join(items))


@command.command()
@click.option('-f', '--file', type=click.File('r'), default=None)
@click.option('-t', '--text', default=None)
def tab_to_space(file,text):
    u"""タブ文字をスペースに置換します。(連続するタブ文字を一つのスペースに置き換え)\n
    example) textutils tab-to-space -t 1\t2\t3 -> 1 2 3

    -f/file : テキストファイルを指定すると、ファイルを読み込み変換して出力します。
        textutils tab-to-space-f filename.txt > out.txt """
    if(not (file or text)):
        lines = click.get_text_stream('stdin').readlines()
    elif(file):
        with file as f:
            lines = f.readlines()
    elif(text):
        lines = [text]

    for line in lines:
        click.echo(" ".join(line.split()))


@command.command()
@click.option('-f', '--file', type=click.File('r'), default=None)
@click.option('-t', '--text', default=None)
def space_to_tab(file, text):
    u"""スペースをタブ文字に置換します。(連続する空白文字を一つのタブに置き換え)\n
    example) textutils space-to-tab -t 1 2 3 -> 1\t2\t3

    -f/file : テキストファイルを指定すると、ファイルを読み込み変換して出力します。
        textutils space-to-tab　-f filename.txt > out.txt """
    if(not (file or text)):
        lines = click.get_text_stream('stdin').readlines()
    elif(file):
        with file as f:
            lines = f.readlines()
    elif(text):
        lines = [text]

    for line in lines:
        click.echo("\t".join(line.split()))


@command.command()
# @click.argument('file', type=click.File('r'))
@click.option('-f', '--file', type=click.File('r'), default=None)
@click.option('-t', '--text', default=None)
def reverse(file, text):
    u"""文字列を逆順にして返します\n
    example) textutils reverse -t 0123456 -> 6543210

    -f/file : テキストファイルを指定すると、中身を読み込み変換して出力します。
        textutils reverse -f filename.txt > out.txt """
    if(not (file or text)):
        lines = click.get_text_stream('stdin').readlines()
    elif(file):
        with file as f:
            lines = f.readlines()
    elif(text):
        lines = [text]

    for line in lines:
        click.echo(line.strip()[::-1])


def main():
    command()

if __name__ == '__main__':
    main()