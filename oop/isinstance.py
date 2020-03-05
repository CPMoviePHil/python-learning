class Website(object):
    pass


class IndexPage(Website):
    pass


class ContactPage(Website):
    pass


index = IndexPage()
print(f'index is instances of IndexPage:{isinstance(index, IndexPage)}')
print(f'index is instances of Website:{isinstance(index, Website)}')
print(f'index is instances of object:{isinstance(index, object)}')
    