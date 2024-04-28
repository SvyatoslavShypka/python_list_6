from read_log import read_lines
from ssh_log_journal import SSHLogJournal


# Funkcja filtrująca logi dla konkretnego adresu IP
def filter_by_ip_address(entry, ip_address):
    if hasattr(entry, 'message') and ip_address in entry.message:
        return True
    elif hasattr(entry, 'error_message') and ip_address in entry.error_message:
        return True
    elif hasattr(entry, 'ip_address') and ip_address in entry.ip_address:
        return True
    else:
        return False


if __name__ == '__main__':
    journal = SSHLogJournal()
    lines = read_lines(None)
    for line in lines:
        journal.append(line)
    print(len(journal))

    for entry in journal:
        print(entry)

    # Filtrowanie logów dla adresu IP 119.137.62.142
    filtered_logs = [entry for entry in journal if filter_by_ip_address(entry, "119.137.62.142")]

    # Sprawdzenie, czy filtrowanie działa poprawnie
    print("-----------------filtered logs-----------------------")
    for entry in filtered_logs:
        print(entry)

    # TEST:    type regexp.log | python ssh_log_journal_test.py
    # TEST:    type SSH.log | python ssh_log_journal_test.py
