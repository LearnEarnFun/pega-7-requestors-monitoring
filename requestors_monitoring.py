from urllib.request import Request, urlopen
import json
from time import sleep
import datetime
from typing import List


def requestors_monitoring(nodes: List[str], period: int):
    while True:
        string_to_write = '{}'.format(datetime.datetime.time(datetime.datetime.now()))
        for node in nodes:
            try:
                node_content = urlopen(Request(node + '/prweb/PRRestService/monitor/pingService/ping')).read().decode("utf-8")
                node_content_dict = json.loads(node_content)
            except Exception as e:
                print('Exception occurred: {};\tString to write: {}'.format(e, string_to_write))
                node_content_dict = {"count": 0}

            string_to_write += ',{}'.format(node_content_dict["count"])

        string_to_write += '\n'

        f = open('requests_history.txt', 'a')
        f.write(string_to_write)
        f.close()

        sleep(period)


if __name__ == '__main__':
    # List of nodes to check browser requestors
    NODES = [
        'http://pega:1111',
    ]

    # Seconds to sleep between checks
    PERIOD = 600

    requestors_monitoring(NODES, PERIOD)
