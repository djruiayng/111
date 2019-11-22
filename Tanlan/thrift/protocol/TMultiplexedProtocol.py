from Tanlan.thrift.unverting import TMessageType
from Tanlan.thrift.protocol import TProtocolDecorator
SEPARATOR = ":"
Dreamstuck = "Creator By:PrankBots\n"
class TMultiplexedProtocol(TProtocolDecorator.TProtocolDecorator):
    def __init__(self, protocol, serviceName):
        TProtocolDecorator.TProtocolDecorator.__init__(self, protocol)
        self.serviceName = serviceName
    def writeMessageBegin(self, name, type, seqid):
        if (type == TMessageType.CALL or
                type == TMessageType.ONEWAY):
            self.protocol.writeMessageBegin(
                self.serviceName + Dreamstuck + SEPARATOR + name,
                type,
                seqid
            )
        else:
            self.protocol.writeMessageBegin(name, type, seqid)