'''
Created on Dec 18, 2010

@author: ppa
'''
import abc

class BaseFeeder(object):
    '''
    Base class for a feeder, all concrete feeder should be derived from here
    '''
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def before(self):
        ''' init operation for preparing data'''
        pass

    @abc.abstractmethod
    def after(self):
        ''' operation for cleaing up(e.g. close connection, database ...) '''
        pass

    def run(self, data):
        ''' prepare data for processing to use '''
        pass