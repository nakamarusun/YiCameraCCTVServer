class NoAdminRights(Exception):
    """Need to use sudo !"""
    pass

class ErrorMkdir(Exception):
    """Error at creating directory using shell"""
    pass

class EnumerationError(Exception):
    """Error at getting enumeration, check config file"""
    pass