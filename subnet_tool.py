#!/usr/bin/bash
"""Tools for working with IP addresses."""

def is_net_valid(network, ip_address):
    """This function takes a network address with CIDR and checks to see if an
    IP is  valid for that network.

    Arguments:
      network: string network address with mask in the form of 8.8.8.0/8

      ip_address: string IP address that should be checked against the network.
      in the form of 192.168.1.1.

    Returns:
      boolean: True if ip is valid for a given range.
    """
    net_ip, mask = network.split("/")[0], network.split("/")[1]
    ip_octet_list = [octet for octet in ip_address.split(".")]
    net_ip_octet_list = [octet for octet in net_ip.split(".")]
    full_mask = int(mask) // 8
    for octet_count in range(full_mask):
        if ip_octet_list[octet_count] != net_ip_octet_list[octet_count]:
            return None
    partial_mask = int(mask) % 8
    if partial_mask == 0:
        return True
    shift = (8 - partial_mask)
    if ((int(net_ip_octet_list[full_mask]) >> shift) ==
            (int(ip_octet_list[full_mask]) >> shift)):
        return True
    return None
