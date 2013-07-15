#!/usr/bin/python
# -*- coding: utf-8 -*-

import colorwin32 as colors

default_colors = colors.get_text_attr()
default_bg = default_colors & 0x0070


def errLog(errText):
    colors.set_text_attr(
        colors.FOREGROUND_RED |
        default_bg |
        colors.FOREGROUND_INTENSITY
    )
    print errText
    colors.set_text_attr(default_colors)


def warnLog(warnText):
    colors.set_text_attr(
        colors.FOREGROUND_YELLOW |
        default_bg |
        colors.FOREGROUND_INTENSITY
    )
    print warnText
    colors.set_text_attr(default_colors)


def sucLog(sucLog):
    colors.set_text_attr(
        colors.FOREGROUND_GREEN |
        default_bg |
        colors.FOREGROUND_INTENSITY
    )
    print sucLog
    colors.set_text_attr(default_colors)


def main():
    print ""
    errLog(u"error")
    sucLog(u"success")
    warnLog(u"warning")

if __name__ == '__main__':
    main()
