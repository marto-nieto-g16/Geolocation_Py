#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import getopt
import sys

version = '1.0'

def obtener_informacion_ip(ip_dns):
    response  = requests.get('http://ip-api.com/json/'+ip_dns)
    if response.status_code == 200:
        json_response = response.json()
        try:
            print ("\n")
            print ("\tIP/DNS Consultada \t: %s" % (str(ip_dns)))
            print ("\tPais(%s) \t\t:: %s" % (str(json_response['countryCode']),str(json_response['country'])))
            print ("\tCiudad \t\t\t:: %s" % (str(json_response['city'])))
            print ("\tISP \t\t\t:: %s" % (str(json_response['isp'])))
            print ("\tOrganizacion \t\t:: %s" % (str(json_response['org'])))
            print ("\tLatitud \t\t:: %s" % (str(json_response['lat'])))
            print ("\tLongitud \t\t:: %s" % (str(json_response['lon'])))
            print ("\tAssociacion \t\t:: %s" % (str(json_response['as'])))
            print ("\tRegion \t\t\t:: %s" % (str(json_response['region'])))
            print ("\tNombre Region \t\t:: %s" % (str(json_response['regionName'])))
            print ("\tZona Horaria \t\t:: %s" % (str(json_response['timezone'])))
            print ("\tCodigo Postal \t\t:: %s" % (str(json_response['zip'])))
            print ("\n")
            return json_response
        except KeyError:
            print('\tError: Direccion IP o DNS Invalido\t\t')
    elif response.status_code == 404:
        print(ip_dns+' No Encontrada.')

options, remainder = getopt.getopt(sys.argv[1:], 'ip:dns', ['dns=', 'version', 'ipaddress=',])
for opt, arg in options:
    if opt in ('-ip', '--ipaddress') :
        obtener_informacion_ip(arg)
    elif opt == '--version':
        print('Version: '+version)