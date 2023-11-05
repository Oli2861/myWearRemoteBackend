import socket

from zeroconf import Zeroconf, ServiceInfo


class ZeroConfWrapper:
    def __init__(self):
        self.zeroconf: Zeroconf = Zeroconf()

        ip: str = socket.gethostbyname(socket.gethostname())
        assert ip != "", "Could not get IP address"
        ip: bytes = socket.inet_aton(ip)

        self.info: ServiceInfo = ServiceInfo(
            type_="_http._tcp.local.",
            name="MyWearRemote._http._tcp.local.",
            addresses=[ip],
            port=5000,
            properties={
                "path": "/",
            },
        )

    def register_service(self):
        print(self.info)
        self.zeroconf.register_service(self.info)
        print(f"Registered service {self.info.name} on {self.info.addresses}:{self.info.port}")

        query_result: ServiceInfo = self.zeroconf.get_service_info(self.info.type, self.info.name)
        print(f"Found the just registered service {query_result.name} on {query_result.addresses}:{query_result.port}")

    def unregister_service(self):
        self.zeroconf.unregister_service(self.info)
        print(f"Unregistered service {self.info.name} on {self.info.addresses}:{self.info.port}")

    def __del__(self):
        self.zeroconf.close()
        print("Closed zeroconf")


if __name__ == "__main__":
    zeroconf = ZeroConfWrapper()
    zeroconf.register_service()
