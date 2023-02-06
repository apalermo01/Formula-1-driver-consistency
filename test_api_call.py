from api_engine import APIEngine
from postgres_login_info import login_info
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

def test_api_call():
    api_caller = APIEngine(login_info)
    params = {}
    api_caller.make_call(tablename='seasons',
                         call_params=params)


def main():
    """main."""
    test_api_call()

if __name__ == '__main__':
    main()
