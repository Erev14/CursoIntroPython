def main():
  # try:
  #   configuration = open('config.txt')
  # except FileNotFoundError as err:
  #   print("Couldn't find the config.txt file!", err)
  # except IsADirectoryError:
  #   print("Found config.txt but it is a directory, couldn't read it")
  # except (BlockingIOError, TimeoutError):
  #   print("Filesystem under heavy load, can't complete reading configuration file")
  # Alternative
  try:
    open("config.txt")
  except OSError as err:
    if err.errno == 2:
      print("Couldn't find the config.txt file!")
    elif err.errno == 13:
      print("Found config.txt but couldn't read it")


if __name__ == '__main__':
    main()