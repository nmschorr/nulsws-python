from jsonSocket import JSONClient
import time
import logging

logger = logging.getLogger("jsonSocket Example")
logger.setLevel(logging.DEBUG)
FORMAT = '[%(asctime)-15s][%(levelname)s][%(funcName)s] %(message)s'

logging.basicConfig(format=FORMAT)


def main():
    logger.debug("starting JSONClient")
    client = JSONClient()
    resultConnect = client.connect()
    logger.debug("connection of the client : {}".format(resultConnect))

    time.sleep(5)

    logger.debug("sending a FALSE closing command ...")

    client.sendObj({"close": False})

    time.sleep(3)

    logger.debug("sending a TRUE closing command ...")

    client.sendObj({"close": True})

    time.sleep(5)

    client.close()


if __name__ == "__main__":
    """client that sends command to the server """
    main()