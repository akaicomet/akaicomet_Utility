import functools
import sys,traceback
from tbvaccine import TBVaccine

def exception(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        #logger = create_logger()
        try:
            return function(*args, **kwargs)          
        except Exception as e:
            if e.errno == 2:
                pass
            else:
                err = "There was an exception in \""
                err += function.__name__ + "\" "

                print(err)
                print(e)
                print(type(e))
                print(e.args)
                print("message:{0}".format(e.with_traceback(sys.exc_info()[2])))
                print(sys.last_value)
                #traceback.print_last()
                #traceback.print_exc()
                # re-raise the exception
                print(TBVaccine().format_exc())
                raise
    return wrapper
