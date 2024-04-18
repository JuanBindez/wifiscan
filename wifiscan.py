import pywifi
from pywifi import const

def scan_wifi_networks():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # obtém a primeira interface Wi-Fi disponível
    iface.scan()
    return iface.scan_results()

def print_wifi_details(networks):
    for network in networks:
        print("SSID:", network.ssid)
        print("BSSID:", network.bssid)
        print("Signal Strength (dBm):", network.signal)
        print("Security:", translate_encryption_type(network.akm))
        print("----------------------------------")

def translate_encryption_type(encryption_type):
    if encryption_type == const.AKM_TYPE_NONE:
        return "Open"
    elif encryption_type == const.AKM_TYPE_WPA:
        return "WPA"
    elif encryption_type == const.AKM_TYPE_WPAPSK:
        return "WPA-PSK"
    elif encryption_type == const.AKM_TYPE_WPA2:
        return "WPA2"
    elif encryption_type == const.AKM_TYPE_WPA2PSK:
        return "WPA2-PSK"
    else:
        return "Unknown"

def main():
    print("Scanning for Wi-Fi networks...")
    available_networks = scan_wifi_networks()
    print("Wi-Fi networks found:")
    print_wifi_details(available_networks)

if __name__ == "__main__":
    main()
