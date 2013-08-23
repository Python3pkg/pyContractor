import inspect
#TODO: make doc of this module

def whoami():
    return inspect.stack()[1][3]

class PyContractor(object):

    @staticmethod
    def require(condition,message=''):
        PyContractor()._evaluate('Pre',condition,message)

    @staticmethod
    def require_not_blank(string,message=''):
        if not string:
            PyContractor()._raiseError('Pre',message,whoami())

    @staticmethod
    def assertExpression(condition, message = ""):
        PyContractor()._evaluate('Assert',condition,message)

    invariant = assertExpression

    @staticmethod
    def ensure(condition, message= ""):
        PyContractor()._evaluate('Post',condition,message)

    def _evaluate(self,type, condition, message):
        """
        :param
        """
        if not condition:
            currentFrame = inspect.currentframe()
            currentFrame = inspect.getouterframes(currentFrame, 2)
            self._raiseError(type,message,currentFrame[1][3])

    def fail(self, message = ''):
        self._raiseError('Fail',message, whoami())

    def _raiseError(self,type,message, caller):
        raise Exception("{0}-condition failed: {1}\nTrace was: {2}".format(type,message,caller))

PRECONDITIONALS = [PyContractor.require,PyContractor.require_not_blank]
POSTCONDITIONALS = [PyContractor.ensure]
CONDITIONALS = [PyContractor.assertExpression]

