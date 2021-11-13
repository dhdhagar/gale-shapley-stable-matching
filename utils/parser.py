import argparse


class BaseParser(argparse.ArgumentParser):
    def __init__(
            self,
            add_main_args=True,
            description='Gale-Shapley parser'):
        super().__init__(
            description=description,
            conflict_handler='resolve',
            formatter_class=argparse.HelpFormatter)

        if add_main_args:
            self.main_args()

    def main_args(self):
        """
        Main program arguments for all scripts.
        """
        parser = self.add_argument_group("Main Arguments")

        parser.add_argument(
            "--silent", action="store_true", help="Hide progress bars."
        )
