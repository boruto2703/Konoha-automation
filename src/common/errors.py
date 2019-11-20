class Error(Exception):
    """ Base class for other exceptions """
    pass


class NotFoundError(Error):
    # print('NotFoundError: Element Not Found')
    pass


class UnClickableError(Error):
    # print('UnClickableError: Element cannot be clicked')
    pass


class TypeError(Error):
    # print('TypeError')
    pass
