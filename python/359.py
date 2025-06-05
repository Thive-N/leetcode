from collections import *


class Logger:
    def __init__(self):
        self.log = defaultdict(str)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.log.keys():
            if self.log[message] <= timestamp-10:
                self.log[message] = timestamp
                return True
            return False
        self.log[message] = timestamp
        return True


if __name__ == "__main__":
    logger = Logger()

    assert logger.shouldPrintMessage(1, "foo") == True    # First time → print
    assert logger.shouldPrintMessage(2, "bar") == True    # First time → print
    # Repeated within 10s → don't print
    assert logger.shouldPrintMessage(3, "foo") == False
    # Repeated within 10s → don't print
    assert logger.shouldPrintMessage(8, "bar") == False
    assert logger.shouldPrintMessage(10, "foo") == False  # Still within 10s
    assert logger.shouldPrintMessage(
        11, "foo") == True   # Now it's been 10s → print
    assert logger.shouldPrintMessage(
        12, "bar") == True   # Now it's been 10s → print
    assert logger.shouldPrintMessage(20, "baz") == True   # New message
    assert logger.shouldPrintMessage(21, "baz") == False  # Within 10s
    assert logger.shouldPrintMessage(31, "baz") == True   # 10s passed

    print("All tests passed.")
