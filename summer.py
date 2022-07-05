def summer(*args1):
    num = args1[0]

    def _sum(*args2):
        if args2:
            return summer(sum([num, *args2]))
        else:
            return num

    return _sum
