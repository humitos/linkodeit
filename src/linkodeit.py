#!/usr/bin/env python

import os
import sys
import json
import logging
import argparse
from urllib import parse, request
from pprint import pprint

URLS = {
    'new': ('POST', 'http://linkode.org/api/1/linkodes/'),
    'create-child': ('POST', 'http://linkode.org/api/1/linkodes/{linkode_id}'),
    'get': ('GET', 'http://linkode.org/api/1/linkodes/{linkode_id}/'),
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Paste a text on linkode.org')

    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('-p', '--parent', type=str,
                        help='linkode id of its parent')
    group.add_argument('-g', '--get', type=str,
                        help='linkode id to get is parent to this new one')

    parser.add_argument('-i', '--input', type=str,
                        help='text file to be pasted on linkode.org')
    parser.add_argument('-t', '--type', type=str,
                        help='the type of the content (plain text, Python, diff, C, etc.)',
                        default='plain text')
    parser.add_argument('-r', '--revision', type=int,
                        default=1,
                        help='the revision number of the node that is parent to this new one')
    parser.add_argument('-v', '--verbose',
                        action='store_true',
                        help='show all the debug information')

    data = {}
    url = URLS['new'][1]

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(
            format='%(levelname)s:%(asctime)s:%(name)s:%(message)s',
            level=logging.DEBUG)

    if args.input:
        if os.path.exists(args.input):
            with open(args.input, 'r') as fh:
                data['content'] = fh.read()
        else:
            print('The file doesn\'t exists.')
    elif not args.get:
        data['content'] = sys.stdin.read()

    data['text_type'] = args.type

    if args.parent:
        method, url = URLS['create-child']
        url = url.format(linkode_id=args.parent)

    if args.revision:
        if args.get:
            print('Ignoring -g / --get argument')
        data['parent'] = args.revision

    if args.get:
        if args.revision:
            print('Ignoring -r / --revision argument')
        method, url = URLS['get']
        url = url.format(linkode_id=args.get)


    print(data)
    print(url)

    raw = parse.urlencode(data).encode('ascii')
    if method == 'POST':
        response = request.urlopen(url, data=raw)
    else:
        response = request.urlopen(url)
    raw = response.read()
    linkode_data = json.loads(raw.decode('utf8'))

    linkode_url = 'http://linkode.org/{}'.format(linkode_data['linkode_id'])
    print(linkode_url)


    # if os.system('whereis xclip') == 0:
    #     os.system('echo {} | xclip'.format(linkode_url))
    #     print('URL copied to clipboard')
