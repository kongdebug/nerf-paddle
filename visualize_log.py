from visualdl.server import app
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='log visulization')

    # params of evaluate
    parser.add_argument(
        "--log_dir", help="The log dir.", default=None, type=str)
    parser.add_argument(
        '--port',
        help='Set the port.',
        type=int,
        default=8040)
    parser.add_argument(
        '--host',
        help='Specify IP address',
        type=str,
        default='127.0.0.1')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()   
    app.run(logdir=args.log_dir, host=args.host, port=args.port)