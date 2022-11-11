
class Result(object):
    def __init__(self, result, order):
        self.result = result
        self.order = order

    def isSuccess(self):
        return self.result.is_success()
        
    def isError(self):
        return self.result.is_error()

    def serialize_errors(self):
        obj_out = {}
        errors = self.result.errors
        
        for err in errors:
            print(dir(err))
            #obj_out['code'] = err['code']

        return obj_out

    def buildsuccessMsg(self):
        pass

    def builderrorMsg(self):
        msg = self.result.errors
        return msg

class Interface(object):

    def _store_create_sucess(self):
        pass

    def cancel_order(self, order):
        pass

    def update_order(self, order):
        pass

    def _store_report(self, order):
        pass
    