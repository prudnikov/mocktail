import logging
import sys

logging.basicConfig(
    level=logging.ERROR,
    handlers=[logging.StreamHandler(sys.stdout)],
    format="~ %(message)s",
)
