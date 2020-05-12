from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder


def main():
    ip = '127.0.0.1'
    port = 6700

    client = udp_client.UDPClient(ip, port)

    args = [0, 228, 123]
    msg = OscMessageBuilder(address='/address')
    msg.add_arg(args)
    m = msg.build()

    client.send(m)


if __name__ == '__main__':
    main()