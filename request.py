import argparse
import requests
import json



def post_state(payload):
    HEADERS = {"Content-Type": "application/json"}
    URL = 'http://localhost:5000/newstate'
    return requests.post(URL, json = payload, headers=HEADERS)



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--productname', help='Product name.', required=True)
    parser.add_argument(
        '--confidence', help='Score', required=True, type=float)
    args = parser.parse_args()

    #ToDo:
    #payload to args.productname & args.confidence

    payload = {'product_name':args.productname, 'confidence': args.confidence}

    r = post_state(payload)
    print(r)
    #ToDo:


if __name__ == '__main__':
  main()
