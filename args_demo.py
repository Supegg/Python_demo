#!/usr/bin/env python

import argparse

if __name__ == "__main__":
    # init
    parser = argparse.ArgumentParser(description="this is a args demo")

    # positional argument, required
    # 位置参数，必选
    parser.add_argument('positional', help="i am required")

    # optional argument, not required except specified required=True
    # 可选参数支持部分匹配，默认None。如 '--op' 在无歧义的时候自动匹配 '--opt'
    # 指定参数类型和范围, it supports common built-in types and functions
    parser.add_argument("-o", "--optional", type=int, default=0,
                        choices=[0, 1, 2], help="i am an optional arg")
    # 打开文件，bar=<_io.TextIOWrapper name='temp.txt' encoding='UTF-8'>
    parser.add_argument('-f', '--file', type=open)
    # The action keyword argument specifies how the command-line arguments should be handled
    # 如果指定参数出现，则action起作用，如果参数不出现default起作用
    parser.add_argument(
        "-b", "--bool", default=1, help="specify a arg", action="store_true")
    
    # 互斥参数组
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    # parse, 先解析可选参数，然后处理位置参数，asc升序进行参数排序
    args = parser.parse_args()
    args1 = parser.parse_args('-v -o 2 he'.split())
    args2 = parser.parse_args(' he -v -o 2'.split())

    print(type(args))
    print(args, args1, args2, sep='\n')


'''
ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])
Define how a single command-line argument should be parsed. Each parameter has its own more detailed description below, but in short they are:

    name or flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
    action - The basic type of action to be taken when this argument is encountered at the command line.
    nargs - The number of command-line arguments that should be consumed.
    const - A constant value required by some action and nargs selections.
    default - The value produced if the argument is absent from the command line.
    type - The type to which the command-line argument should be converted.
    choices - A container of the allowable values for the argument.
    required - Whether or not the command-line option may be omitted (optionals only).
    help - A brief description of what the argument does.
    metavar - A name for the argument in usage messages.
    dest - The name of the attribute to be added to the object returned by parse_args().

    
    https://blog.csdn.net/liuweiyuxiang/article/details/82918911
    https://docs.python.org/3/library/argparse.html

'''
