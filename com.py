# import wifi something ;)

# Note that this or lower modules implement the protocol dteials...
# the interface provides an apstract to basic in/output

class robocom(object):
    '''polimorph com object (wifi,bt,eth)'''
    def __init__(self):
        self._cmd  = 0
        self._attr = +

        # init wifi, bt, or eth setting up socket
        # init_wifi()

    def input():
        # do communication with outer world here
        
        # TODO: implement me with wifi, bt, or eth...
        # either client server protocol receive
        # combined in transmit call...
        
        # receive_wifi()
        
        # or producer consumer where robot is consumer
        # taking incomming events from a queue produced
        # by wifi, bt or eth task in the background ;)

        # read_queue()             

        # update next robo command generated from above
        # functions...
        self._cmd  = REMOTE
        self._attr = FOR

    def output():
        # here comes the send() call implementation which is
        # just needed if client server approach is used

    def get_cmd():
        return self._cmd

    def get_attr():
        return self._attr
