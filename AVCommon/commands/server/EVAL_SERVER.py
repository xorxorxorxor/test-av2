from AVCommon.logger import logging


def execute(vm, protocol, args):
    """ client side, returns (bool,*) """
    #logging.debug("    CS Execute")
    assert vm, "null vm"

    ret = eval(args)
    return True, ret

