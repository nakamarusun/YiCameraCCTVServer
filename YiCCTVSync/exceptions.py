class NoAdminRights(Exception):
    """Need to use sudo !"""
    pass

class ErrorMkdir(Exception):
    """Error at creating directory using shell"""
    pass