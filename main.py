#    Author:   Xinyi Hu
#    Contact:  xinyih20@uci.edu

from utils.db import DB
from resources.tables import *
from utils.log import Log
from gui.DBFramework import demo

logger = Log("Main function")


def load_db():
    stu_db = DB('stu')
    stu_db.select(TABLE_STU)
    stu_db.select(TABLE_COURSE)
    stu_db.select(STU_TABLE_COURSE)
    logger.info("Tables are created;")


if __name__ == '__main__':
    load_db()
    demo()