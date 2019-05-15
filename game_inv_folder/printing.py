import reports


def inputs(s = None):
    args = []
    args.append(input("Filename: "))
    if(s != None): args.append(input(s))
    return args


while True:
    print("--------------\n" +
          "1) Count games\n" +
          "2) Decide by year\n" +
          "3) Get latest\n" +
          "4) Count by genre\n" +
          "5) Get line number by title\n" +
          "6) Sort ABC\n" +
          "7) Get genres\n" +
          "8) When was top sold FPS")
    selected = input("> ")

    try:
        if(selected == '1'):
            args = inputs()
            print(reports.count_games(args[0]))
        elif(selected == '2'):
            args = inputs("Year: ")
            print(reports.decide(args[0], args[1]))
        elif(selected == '3'):
            args = inputs()
            print(reports.get_latest(args[0]))
        elif(selected == '4'):
            args = inputs("Genre: ")
            print(reports.count_by_genre(args[0], args[1]))
        elif(selected == '5'):
            args = inputs("Title: ")
            print(reports.get_line_number_by_title(args[0], args[1]))
        elif(selected == '6'):
            args = inputs()
            print(reports.sort_abc(args[0]))
        elif(selected == '7'):
            args = inputs()
            print(reports.get_genres(args[0]))
        elif(selected == '8'):
            args = inputs()
            print(reports.when_was_top_sold_fps(args[0]))
        else:
            continue
    except Exception as ex:
        print(ex)