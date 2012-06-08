'''
Created on 5 avr. 2012

@author: damienp
'''

class SafeEvalException(Exception):
    def __init__(self):
        self.message = "SafeEvalException"
        
    def __str__(self):
        return self.message

class SafeEvalExecException(SafeEvalException):
    """
    Exception class for reporting all errors which occured while
    validating AST for source code in safe_eval().

    Attributes:
      errors = encapsulation of the error
    """
    def __init__(self, errors):
        super(SafeEvalExecException, self).__init__()
        self.errors = errors
        self.message = '\n'.join([str(err) for err in self.errors])

class SafeEvalCodeException(SafeEvalException):
    """
    Exception class for reporting all errors which occured while
    validating AST for source code in safe_eval().

    Attributes:
      code   = raw source code which failed to validate
      errors = list of SafeEvalError
    """
    def __init__(self, code, errors):
        super(SafeEvalCodeException, self).__init__()
        self.code, self.errors = code, errors
        self.message = '\n'.join([str(err) for err in self.errors])


class SafeEvalContextException(SafeEvalException):
    """
    Exception class for reporting unallowed objects found in the dict
    intended to be used as the local enviroment in safe_eval().

    Attributes:
      keys   = list of keys of the unallowed objects
      errors = list of strings describing the nature of the error
               for each key in 'keys'
    """
    def __init__(self, keys, errors):
        super(SafeEvalContextException, self).__init__()
        self.keys, self.errors = keys, errors
        self.message = '\n'.join([str(err) for err in self.errors])
        
class SafeEvalTimeoutException(SafeEvalException):
    """
    Exception class for reporting that code evaluation execeeded
    the given timelimit.

    Attributes:
      timeout = time limit in seconds
    """
    def __init__(self, timeout):
        super(SafeEvalTimeoutException, self).__init__()
        self.timeout = timeout
        self.message = "Timeout limit execeeded (%s secs) during exec" % self.timeout
