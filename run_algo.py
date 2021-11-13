from utils.parser import BaseParser


def main(params):
    # TODO
    print()


if __name__ == "__main__":
    parser = BaseParser()
    args = parser.parse_args()
    print(args)
    main(args.__dict__)
