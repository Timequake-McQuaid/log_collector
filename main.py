
# open file either using relative path as done here or bring file to this folder
with open("../../../../../var/log/syslog.1", "r") as file:
    sysdata = file.readlines()
    # if this file does not exist, it will create it in the current dir
    with open("syslog.txt", "r+", encoding="utf-8") as outfile:
        for each in sysdata:
            # search for a string inside the file by iterating through the lines
            if "ERROR" in each:
                outfile.write(f"{each}\n")
            