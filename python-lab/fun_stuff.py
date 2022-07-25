import copy
from inspect import signature
count_arguments = lambda fun: len([i for i in str(signature(fun)).replace('(','').replace(')','').split(',') if i != ''])
function = type(lambda:1)
class Maybe:
    def __init__(self, value, no_nest = True):
        self.value = value
        if type(self.value) == Maybe and no_nest == True: self.value = self.value.unwrap()
        self.unwrap = lambda : self.value

    def expect(self, fun = None):  
                if (type(self.value) == type(Exception)) and fun == None: raise self.value
                elif (self.value == None) and fun == None: raise Exception("Found 'None' on expect")
                elif (self.value == '') and fun == None: raise Exception("Found empty string on expect")
                elif (type(self.value) == type(Exception) or self.value == '' or self.value == None): return fun(self.value)
                else: return self.value 


    def bind(self, fun):
        try:
            return Maybe(fun(self.value)) if self.value != None else  Maybe(None)
        except Exception as err:
            return Maybe(err)
    def bind_or(self, fun, default, call = True):
        if type(default) != function or call == False:
            try:
                return Maybe(fun(self.value)) if self.value != None else  Maybe(default)
            except Exception as err:
                return Maybe(default)
        elif count_arguments(default) < 1:
            try:
                return Maybe(fun(self.value)) if self.value != None else  Maybe(default())
            except Exception as err:
                return Maybe(default())
        else:
            try:
                return Maybe(fun(self.value)) if self.value != None else  Maybe(default(*[Maybe(self.value).unwrap(), Exception("Found value 'None'"), fun, default][0:count_arguments(default)]))
            except Exception as err:
                print("foo")
                return Maybe(default(*[Maybe(self.value).unwrap(), err, fun, default][0:count_arguments(default)]))
    def unwrap_or(self, default):
        return Maybe(self.value).bind_or(lambda x: x, default).unwrap()





    def __repr__(self):
        return f'Maybe({self.value})'

handle = lambda x, y, err: Maybe(Exception(f'{type(err)}:{err}, folded: {x}, Next: {y}')) 
class Iter: 
    def __init__(self, values):
        self.values = Maybe(values)
        self.unwrap = lambda : [Maybe(i).unwrap() for i in self.values.unwrap()]
        self.unwrap_or = lambda default : [Maybe(i).unwrap_or(default) for i in self.values.unwrap() ]
        self.filter = lambda fun : Iter([Maybe(i) for i in self.values.unwrap() if Maybe(i).bind_or(fun, False).unwrap()])
        self.count = lambda fun = None: len(self.values.unwrap()) if fun == None else len(self.filter(fun).unwrap())
    def fold(self, init, fun, handle=handle):
        ini = copy.deepcopy(init)
        count = -1
        for i in self.values.unwrap():
            count +=1
            try:
                ini = fun(Maybe(ini).unwrap(),Maybe(i).unwrap())
            except Exception as err: 
                if count_arguments(handle) > 0:
                    ini = handle(*[Maybe(ini).unwrap(),Maybe(i).unwrap(), err, count][0:count_arguments(handle)])
                else: ini = handle()
 
        return Maybe(ini)            

    def reduce(self, fun, handle = handle):
        ini = Maybe(self.values).unwrap()[0] if len(Maybe(self.values).unwrap()) > 0 else None
        if Maybe(ini).unwrap() == None: return Maybe(None)

        count = -1
        for i in self.values.unwrap()[1:]:
            count +=1
            try:
                ini = fun(Maybe(ini).unwrap(),Maybe(i).unwrap())
            except Exception as err:
                if count_arguments(handle) > 0:
                    ini = handle(*[Maybe(ini).unwrap(),Maybe(i).unwrap(), err, count][0:count_arguments(handle)])
                else: ini = handle()
 
        return Maybe(ini)
    
    def map(self, fun, handle = None):
        out = []
        if Maybe(ini).unwrap() == None: return Iter([Maybe(None)])

        count = -1
        for i in self.values.unwrap():
            count +=1
            try:
                 out.append(Maybe(fun(Maybe(i).unwrap())))
            except Exception as err:
                if type(handle) == function:
                    if count_arguments(handle) > 0:
                        out.append( Maybe(handle(*[Maybe(out).unwrap(), Maybe(i).unwrap(), err, count][0:count_arguments(handle)])))
                    else: out.append(Maybe(handle()))
                elif Maybe(i).unwrap() == None: 
                    out.append(Maybe(None))
                else: out.append(Maybe(err))
 
        return Iter(out)

           
