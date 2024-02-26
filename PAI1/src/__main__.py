import gui, config, scan, compare, schedule, time, send_mail
from datetime import datetime

def monthly_mail():
    today = datetime.today()
    if today.day == 1:
        conf = config.readConfig()
        recipient = conf['hids']['email_to_notify']
        send_mail.send_email(recipient)
        print("Monthly report was sent.")
        with open("log.log", 'w') as log_file:
            log_file.write("")
            print("Log file cleared.")


def daily_scan():
    print("Scan is running...")
    conf = config.readConfig()
    dict_new_hashes = scan.scan_all_files(conf["hids"]["directories_to_scan"], conf["hids"]["hash_function"], True, False)
    compare.compare_hashes(dict_new_hashes)
    print("Daily scan is finished.")


def main():
    conf = config.writeDefaultConfig()
    gui.startGUI()
    scan.scan_all_files(conf["hids"]["directories_to_scan"], conf["hids"]["hash_function"], False, True)
    print("Basic scan finished.")
    compare.initialize_log()
    print("Log initialized.")
    

# schedule the scans
    scan_interval = conf["hids"]["scan_interval"]
    # normally 3 means testing daily, here only 10 seconds for testing purposes because 3 is default value
    if scan_interval == "1":
        schedule.every(3).minutes.do(daily_scan)  
    elif scan_interval == "2":
        schedule.every(1).hour.do(daily_scan)
    else:
        # schedule.every(3).minutes.do(daily_scan)
        schedule.every().day.at("23:59").do(daily_scan)

# schedule the emails for testing purpose
    log_interval = conf['hids']['log_interval']
    if log_interval == "1":
        schedule.every(10).minutes.do(monthly_mail)
    elif log_interval == "2":
        schedule.every(34).hours.do(monthly_mail)
    else:
        schedule.every().day.at("00:00").do(monthly_mail)
        # schedule.every(30).minutes.do(monthly_mail)


    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()
