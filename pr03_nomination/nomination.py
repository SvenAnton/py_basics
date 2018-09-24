"""See on kodutöö PR03."""


import time


def ask_name():
    """"Funktsioon, mis küsib nime."""
    while True:
        name = input("What is your full name, dear fellow?").strip()
        is_title = name.istitle()
        is_spaced = name.find(" ") != -1
        is_alpha = name.replace(" ", "").replace("-", "").isalpha()
        if is_title and is_spaced and is_alpha:
            return name
        else:
            print("Sorry, try again.")


def progress_bar(process_name, seconds):
    """""Funktsioon, mis teeb progress bar'i."""
    cycle_time = seconds / 20

    chr_limit = 25
    is_long = len(process_name) > chr_limit - 2

    if is_long:
        process_name = f"{process_name[:chr_limit - 5]}..."

    for i in range(21):
            print(f"\r[{'|' * i:-<20}] | Process: {process_name!r:.{chr_limit}} {0.05 * i:4.0%}", end='')
            time.sleep(cycle_time)
    print()


def print_ok():
    """"Funktsioon, mis ütleb, kui nimi sisestatud."""
    print("Nominee listed.")


def main():
    """"Funktsioon, mis käivitab kõik teised funktsioonid soovitud järjekorras."""
    ask_name()
    progress_bar("Setting up the nominee", 5)
    print_ok()


if __name__ == "__main__":
    main()
