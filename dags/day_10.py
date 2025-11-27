from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 10th")
def day_10():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-10":
            print("It is December 10th! Let me open the window!")
        elif today > "2025-12-10":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def santa_claus_is_comin_to_town_1():
        print("You'd better watch out, you'd better not cry")
        
    @task
    def santa_claus_is_comin_to_town_2():
        print("You'd better not pout, I'm telling you why")
        
    @task
    def santa_claus_is_comin_to_town_3():
        print("Santa Claus is coming to town!")
        
    @task
    def santa_claus_is_comin_to_town_4():
        print("He's making a list, he's checkin' it twice")
        
    @task
    def your_song_for_today():
        print("Today's song is Santa Claus Is Comin' to Town by The Crystals!")
        print("Listen here: https://www.youtube.com/watch?v=FK2tcFFB6ZM")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _scictt_1 = santa_claus_is_comin_to_town_1()
    _scictt_2 = santa_claus_is_comin_to_town_2()
    _scictt_3 = santa_claus_is_comin_to_town_3()
    _scictt_4 = santa_claus_is_comin_to_town_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _scictt_1, _scictt_2, _scictt_3, _scictt_4, _your_song_for_today, _opening_the_window)


day_10()
