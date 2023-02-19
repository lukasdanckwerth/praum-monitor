import os
from datetime import datetime, date
from pathlib import Path


def is_dir(path):
    return Path(path).is_dir()


def is_file(path):
    return Path(path).is_file()


def create_if_not_exists(path):
    if not is_dir(path):
        os.mkdir(path)


def current_year():
    return date.today().strftime("%Y")


def current_month():
    return date.today().strftime("%m")


class DataDirectory():

    def __init__(self, path):
        self.path = path
        self.records_count = 0
        self.start_time = datetime.now()
        self.start_time_formatted = self.start_time.strftime("%Y-%m-%d-%H-%M-%S")

        create_if_not_exists(path)
        create_if_not_exists(self.current_year_dir())
        create_if_not_exists(self.current_month_dir())

        self.last_session_file = self.last_session_file_path()
        self.create_session_file()

        print("DataDirectory")
        print("Start time: " + self.start_time_formatted)
        print("Last session file: " + self.last_session_file)
        print("")

    def current_year_dir(self):
        return self.path + "/" + current_year()

    def current_month_dir(self):
        return self.current_year_dir() + "/" + current_month()

    def status_file_path(self):
        return self.path + "/status.txt"

    def write_status_file(self, content):
        f = open(self.status_file_path(), "w")
        f.write(content)
        f.close()

    def session_file_path(self):
        return self.current_month_dir() + "/" + self.start_time_formatted + ".csv"

    def create_session_file(self):
        self.append_session_file("")
        self.create_last_session_file()

    def append_session_file(self, content):
        f = open(self.session_file_path(), "a")
        f.write(content)
        f.close()

    def last_session_note(self):
        return self.path + "/last_session.txt"

    def create_last_session_file(self):
        f = open(self.last_session_note(), "w")
        f.write(self.session_file_path())
        f.close()

    def last_session_file_path(self):
        if is_file(self.last_session_note()):
            return open(self.last_session_note(), "r").read()
        return ""

    def add_record(self, content):
        self.write_status_file(content)
        self.append_session_file(content)
        self.records_count += 1
