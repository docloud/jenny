# coding=utf8

"""
Copyright 2015 jenny
"""

import pandoc
import subprocess


def compile(content, input_format, output_format, *args):

    subprocess_arguments = ['pandoc',
                            '--from=%s' % input_format,
                            '--to=%s' % output_format]
    subprocess_arguments.extend(args)
    p = subprocess.Popen(
            subprocess_arguments,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
    )
    return p.communicate(content)[0]
