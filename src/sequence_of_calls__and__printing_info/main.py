"""
Sequence of calls to functions __init__ and __init_subclass__ in case of multiple inheritance.
And printing some info.
"""


# --------------------------------------------------
def print_info_for_cls(cls, super):
    print('    cls                   =', cls)
    print('    cls.__mro__           =', cls.__mro__)
    print('    cls.__bases__         =', cls.__bases__)
    print('    cls.__base__          =', cls.__base__)
    print('    super()               =', super)
    print('    super().__thisclass__ =', super.__thisclass__)


def print_info_for_self(self, super):
    print('    self                     =', self)
    print('    self.__class__           =', self.__class__)
    print('    self.__class__.__mro__   =', self.__class__.__mro__)
    print('    self.__class__.__bases__ =', self.__class__.__bases__)
    print('    self.__class__.__base__  =', self.__class__.__base__)
    print('    super()                  =', super)
    print('    super().__thisclass__    =', super.__thisclass__)
# --------------------------------------------------


# --------------------------------------------------
class Base:
    def __init__(self):
        print('< Base.__init__')
        print_info_for_self(self=self, super=super())
        super().__init__()
        print('> Base.__init__')


class MixinA:
    def __init__(self):
        print('< MixinA.__init__')
        print_info_for_self(self=self, super=super())
        super().__init__()
        print('> MixinA.__init__')

    @classmethod
    def __init_subclass__(cls):
        print('< MixinA.__init_subclass__')
        print_info_for_cls(cls=cls, super=super())
        super().__init_subclass__()
        print('> MixinA.__init_subclass_')


class MixinB:
    def __init__(self):
        print('< MixinB.__init__')
        print_info_for_self(self=self, super=super())
        super().__init__()
        print('> MixinB.__init__')

    @classmethod
    def __init_subclass__(cls):
        print('< MixinB.__init_subclass__')
        print_info_for_cls(cls=cls, super=super())
        super().__init_subclass__()
        print('> MixinB.__init_subclass__')
# --------------------------------------------------


# --------------------------------------------------
class MyClass(Base, MixinA, MixinB):
    def __init__(self):
        print('< MyClass.__init__')
        print_info_for_self(self=self, super=super())
        super().__init__()
        print('> MyClass.__init__')
# --------------------------------------------------


if __name__ == '__main__':
    my_class = MyClass()

"""
You will see the following:

< MixinA.__init_subclass__
    cls                   = <class '__main__.MyClass'>
    cls.__mro__           = (<class '__main__.MyClass'>, <class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>, <class 'object'>)
    cls.__bases__         = (<class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>)
    cls.__base__          = <class '__main__.Base'>
    super()               = <super: <class 'MixinA'>, <MyClass object>>
    super().__thisclass__ = <class '__main__.MixinA'>
< MixinB.__init_subclass__
    cls                   = <class '__main__.MyClass'>
    cls.__mro__           = (<class '__main__.MyClass'>, <class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>, <class 'object'>)
    cls.__bases__         = (<class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>)
    cls.__base__          = <class '__main__.Base'>
    super()               = <super: <class 'MixinB'>, <MyClass object>>
    super().__thisclass__ = <class '__main__.MixinB'>
> MixinB.__init_subclass__
> MixinA.__init_subclass_
< MyClass.__init__
    self                     = <__main__.MyClass object at 0x000001672088AA60>
    self.__class__           = <class '__main__.MyClass'>
    self.__class__.__mro__   = (<class '__main__.MyClass'>, <class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>, <class 'object'>)
    self.__class__.__bases__ = (<class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>)
    self.__class__.__base__  = <class '__main__.Base'>
    super()                  = <super: <class 'MyClass'>, <MyClass object>>
    super().__thisclass__    = <class '__main__.MyClass'>
< Base.__init__
    self                     = <__main__.MyClass object at 0x000001672088AA60>
    self.__class__           = <class '__main__.MyClass'>
    self.__class__.__mro__   = (<class '__main__.MyClass'>, <class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>, <class 'object'>)
    self.__class__.__bases__ = (<class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>)
    self.__class__.__base__  = <class '__main__.Base'>
    super()                  = <super: <class 'Base'>, <MyClass object>>
    super().__thisclass__    = <class '__main__.Base'>
< MixinA.__init__
    self                     = <__main__.MyClass object at 0x000001672088AA60>
    self.__class__           = <class '__main__.MyClass'>
    self.__class__.__mro__   = (<class '__main__.MyClass'>, <class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>, <class 'object'>)
    self.__class__.__bases__ = (<class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>)
    self.__class__.__base__  = <class '__main__.Base'>
    super()                  = <super: <class 'MixinA'>, <MyClass object>>
    super().__thisclass__    = <class '__main__.MixinA'>
< MixinB.__init__
    self                     = <__main__.MyClass object at 0x000001672088AA60>
    self.__class__           = <class '__main__.MyClass'>
    self.__class__.__mro__   = (<class '__main__.MyClass'>, <class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>, <class 'object'>)
    self.__class__.__bases__ = (<class '__main__.Base'>, <class '__main__.MixinA'>, <class '__main__.MixinB'>)
    self.__class__.__base__  = <class '__main__.Base'>
    super()                  = <super: <class 'MixinB'>, <MyClass object>>
    super().__thisclass__    = <class '__main__.MixinB'>
> MixinB.__init__
> MixinA.__init__
> Base.__init__
> MyClass.__init__
"""
