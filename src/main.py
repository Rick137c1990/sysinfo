import sysinfo

def main()-> None:
    info = sysinfo.get_info()
    for sections, values in info.items():
        print(f"\n{'=' * 15} {sections} {'=' * 15}")
        for key, value in values.items():
            print(f"{key:15}: {value}")

if __name__ == "__main__":
    main()


