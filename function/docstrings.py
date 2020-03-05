def driver_test(name='', licence=False, alcohol=0):
    '''
    :param name: Get the driver name
    :param licence: Get the status of driver's licence
    :param alcohol: get the current status of driver physics
    :return: nothing, only for print out the status of driver can drive or not
    '''
    name = name
    licence = licence
    alcohol = alcohol
    if licence is True and alcohol <= 0:
        print(f'Driver {name} now can drive the car')


# driver_test('phil', True, 0)
help(driver_test)
print(driver_test.__doc__)
