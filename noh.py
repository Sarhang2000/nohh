def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(24):
        for fg in range(00, 60):
            s1 = ''
            for bg in range(00, 60):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')
 
 
print_format_table()