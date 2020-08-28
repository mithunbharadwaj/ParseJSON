import json
import socket
import mysql.connector

with open('/Users/MITHUN/PycharmProjects/ParseJSON/sample-data.json') as access_json:
    x = json.load(access_json)
    sql_stm = []
    sql_dict = {}

#comment come mf
def getCPU(y):
        state = y['state']
        if not (state is None):
            state = y['state']

            memory = state['memory']
            mem_usage = memory['usage']

            ip_List4 = []
            ip_List6 = []

            network = state['network']
            for network_instance in network:
                instance = network[network_instance]
                addresses = instance['addresses']
                for single_address in addresses:
                    ip = single_address['address']
                    family = single_address['family']
                    try:
                        socket.inet_pton(socket.AF_INET,ip)
                        ip_List4.append(ip)
                    except:
                        pass

                    try:
                        socket.inet_pton(socket.AF_INET6,ip)
                        ip_List6.append(ip)
                    except:
                        pass

            cpu = state['cpu']
            usage = cpu['usage']

            sql_stm.append(usage)
            sql_dict['memory'] = mem_usage
            sql_dict['ipList4'] = ip_List4
            sql_dict['ipList6'] = ip_List6
            sql_dict['cpu'] = usage;
        else:
            sql_stm.append('N/A')
            sql_dict['cpu'] = 'N/A'

def getStatus(y):
        status = y['status']
        if not (status is None):
            sql_stm.append(status)
            sql_dict['status'] = status;


def getCreated_at(y):
    created_att = y['created_at']
    sql_stm.append(created_att)
    sql_dict['created'] = created_att;
    #print(sql_stm)


def getName(y):
    getTheName = y['name']
    sql_stm.append(getTheName)
    sql_dict['name'] = getTheName

#def getIpaddress():



SQLDict = []
SQLList = []
for y in x:
    getStatus(y)
    getName(y)
    getCPU(y)
    getCreated_at(y)
    SQLList.append(sql_stm)
    SQLDict.append(sql_dict)
    sql_stm = []
    sql_dict = {}

for one_sql in SQLDict:
    print(one_sql)




"""
for y in range(16):
    getStatus(x[y])
    getName(x[y])
    getCPU(x[y])
    getCreated_at(x[y])
    print(sql_stm)
"""










