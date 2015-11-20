#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import requests
import argparse

def parse_cmd_args():
    '''Return command arguments.'''
    parser = argparse.ArgumentParser(description='''testlb is a command for displaying stats on connections through loadbalancer.''', add_help=False)
    parser.add_argument('-h','--host', help='''Host address to run against.''',required=True)
    parser.add_argument('-n','--num', help='How many requests should we do?', type=int, default=100, required=False)
    args = parser.parse_args()
    return args

def _do_request(url):
    '''Perform the request and return text.'''
    try:
        r = requests.get(url)
        return r.text
    except requests.exceptions.ConnectionError as e:
        print('Unable to connect to {0} {1}'.format(url, e))
        sys.exit(2)
    except:
        raise

def _format_output(data):
    '''Sort dict data and return list'''
    out = []
    for item in sorted(data):
        txt = ('{0}: {1}'.format(item, data[item]))
        out.append(txt)
    return out

def main():
    args = parse_cmd_args()
    stats_dict = {}
    url = 'http://{0}'.format(args.host)
    for i in range(args.num):
        node = _do_request(url).rstrip()
        if node not in stats_dict:
            stats_dict[node] = 1
        else:
            stats_dict[node] += 1
        output = _format_output(stats_dict)
    print('\n'.join(output))

if __name__ == '__main__':
    main()