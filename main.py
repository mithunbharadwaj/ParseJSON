import json
import sys

import mongo
import pymongo
from pymongo import MongoClient


# Get performance statistics - cpu, memory, addresses
def get_stats(y):
    # Returned crate, initialized to defaults
    ret_crate = {'cpu': "N/A", 'memory_usage': "N/A", 'ip_addresses': []}

    # Check if there is a state, if not, return an empty crate
    state = y['state']
    if state is None:
        return ret_crate

    # Check for memory usage
    memory = state['memory']
    if memory is not None:
        mem_usage = memory['usage']
        if mem_usage is not None:
            ret_crate['memory_usage'] = mem_usage

    # Get lists of IP addresses
    network = state['network']
    if network is None:
        pass
    else:
        for network_instance in network:
            instance = network[network_instance]
            addresses = instance['addresses']
            for single_address in addresses:
                ip = single_address['address']
                # print(ip)
                ret_crate['ip_addresses'].append(ip)

    # Get CPU usage if available
    cpu = state['cpu']
    if cpu is not None:
        usage = cpu['usage']
        if usage is not None:
            ret_crate['cpu'] = usage

    # Return the final crate
    return ret_crate


def get_status(y):
    status = y['status']
    if status is None:
        return "N/A"
    else:
        return status


def get_creation_time(y):
    created_at = y['created_at']
    if created_at is None:
        return "N/A"
    else:
        return created_at


def get_name(y):
    name = y['name']
    if name is None:
        return "N/A"
    else:
        return name


# -----------------------------------------------------------------------------------------------------------------------
# Mainline code
# -----------------------------------------------------------------------------------------------------------------------

# Command line parameters
# main.py [json-file] [mongo db url]
# Defaults: sample-data.json 127.0.0.1

json_file_spec = "sample-data.json"
mongo_url="127.0.0.1"

if len(sys.argv)==1:
    pass
elif len(sys.argv)==2:
    json_file_spec=sys.argv[1]
elif len(sys.argv)==3:
    json_file_spec=sys.argv[1]
    mongo_url=sys.argv[2]
else:
    pass

# Print the command line arguments
print("Json-file: " + json_file_spec + " MongoDB URL: " + mongo_url)

# Open the JSON file and parse it with standard library
with open(json_file_spec) as access_json:
    input_json = json.load(access_json)

access_json.close()

output_records = []

for record in input_json:
    status = get_status(record)
    name = get_name(record)
    stats = get_stats(record)
    created_at = get_creation_time(record)

    # Create final output record
    output_record = {}

    output_record['status'] = status
    output_record['name'] = name
    output_record['created_at'] = created_at

    output_record['cpu'] = stats['cpu']
    output_record['memory_usage'] = stats['memory_usage']
    output_record['ip_addresses'] = stats['ip_addresses']

    output_records.append(output_record)

# Print to the standard output for debugging and diagnostics
count = 0
for one_record in output_records:
    print(str(count) + ": " + str(one_record))
    count = count + 1

# Connect to the Mongo database (localhost) and insert all output records as documents to
# the database
try:
    client = MongoClient(mongo_url)
    client.drop_database("json_test_db")
    database = client.get_database("json_test_db")
    collection = database.get_collection("json_test_collection")
    collection.insert_many(output_records)

    # Run query command to verify documents are in the database, display no of documents
    cursor = collection.find()
    doc_count=0;
    for doc in cursor:
        print(doc)
        doc_count=doc_count+1
    print("Documents retrieved: "+ str(doc_count))

except:
    print("Connection to the database failed")
    print(str(sys.exc_info()))
    exit(-1)
