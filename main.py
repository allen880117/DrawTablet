# -*- coding: utf-8 -*-
import DrawTablet as DT
from datetime import datetime


def main():
    log_file_path = 'log/log_'+datetime.now().strftime("%Y-%m-%d_%H%M%S").__str__()+'.txt'
    dt = DT.DrawTablet(log_file_path)
    try:
        dt.run()
    finally:
        dt.log_dump()


if __name__ == "__main__":
    main()
