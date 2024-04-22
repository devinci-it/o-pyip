import logging
import netifaces


class NetworkInterfaceManager:

    """
    A class to manage network interfaces.

    This class provides methods to set IP addresses for network interfaces
    and retrieve information about available network interfaces.

    Attributes:
        logger: A logger object for logging messages.
        interface_data: A list to store interface data.
        log_messages: A list to store log messages.
        interfaces: A list of available network interfaces.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.interface_data = None
        self.log_messages = []
        self.interfaces = netifaces.interfaces()

    def set_ip_address(self, interface_name, ip_address, netmask):
        """
        Set the IP address for a given network interface.

        Args:
            interface_name (str): The name of the network interface.
            ip_address (str): The IP address to set.
            netmask (str): The netmask for the IP address.

        Returns:
            None
        """
        log_message = f"Interface {interface_name} configured with IP: {ip_address} and Netmask: {netmask}"
        self.log_messages.append(log_message)
        self.logger.info(log_message)

    def retrieve_interface_data(self):
        """
        Retrieve data about available network interfaces.

        This method retrieves data about available network interfaces,
        including their IP addresses, netmasks, DNS servers, and default gateway.

        Returns:
            list: A list of lists containing interface data.
        """
        self.__list_interfaces()
        if self.interface_data:
            self.logger.info('Data retrieved from private method')
            return self.interface_data
        else:
            self.logger.error('Exception occurred')

    def __list_interfaces(self):
        """
        List available network interfaces and their information.

        This method lists available network interfaces and retrieves
        information such as IP addresses, netmasks, DNS servers, and default gateway.

        Raises:
            RuntimeError: If no network interfaces are available or if permission is denied.
        """
        try:
            self.interface_data = []  # Clear existing data
            gateways = netifaces.gateways()
            default_gateway = gateways.get('default', [])
            if default_gateway:
                default_gateway = default_gateway[netifaces.AF_INET][0][0]
            else:
                default_gateway = "None"

            for interface_name in netifaces.interfaces():
                if netifaces.AF_INET in netifaces.ifaddresses(interface_name):
                    ip_address = netifaces.ifaddresses(interface_name)[netifaces.AF_INET][0]['addr']
                    netmask = netifaces.ifaddresses(interface_name)[netifaces.AF_INET][0]['netmask']

                    # Retrieve DNS servers (IPv4 addresses)
                    dns_servers = ", ".join(
                        [dns_data['addr'] for dns_data in
                         netifaces.ifaddresses(interface_name).get(netifaces.AF_INET, [])]
                    )

                    self.interface_data.append([interface_name, ip_address, netmask, dns_servers, default_gateway])

            if not self.interface_data:
                raise RuntimeError("No network interfaces available")

            return self.interface_data
        except PermissionError:
            raise RuntimeError("Permission denied: Unable to access network interfaces. Try running with sudo.")
        except RuntimeError as e:
            raise e
