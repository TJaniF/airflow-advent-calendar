from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 24th")
def day_24():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-24":
            print("It is December 24th! Let me open the window!")
        elif today > "2025-12-24":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def zat_you_santa_claus_1():
        print("'Zat You, Santa Claus?")
        
    @task
    def zat_you_santa_claus_2():
        print("Gifts I'm preparing for some Christmas sharing")
        
    @task
    def zat_you_santa_claus_3():
        print("But I pause because")
        
    @task
    def zat_you_santa_claus_4():
        print("Hanging my stocking I can hear a knocking")
        
    @task
    def your_song_for_today():
        print("Today's song is Zat You Santa Claus by Louis Armstrong!")
        print("Listen here: https://www.youtube.com/watch?v=cqIpxPvhb_8")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _zysc_1 = zat_you_santa_claus_1()
    _zysc_2 = zat_you_santa_claus_2()
    _zysc_3 = zat_you_santa_claus_3()
    _zysc_4 = zat_you_santa_claus_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _zysc_1, _zysc_2, _zysc_3, _zysc_4, _your_song_for_today, _opening_the_window)


day_24()
