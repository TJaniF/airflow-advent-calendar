from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 1st")
def day_1():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-01":
            print("It is December 1st! Let me open the window!")
        elif today > "2025-12-01":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today


    @task
    def winter_wonderland_1():
        print("Sleigh bells ring, are you listenin'")
        
    @task
    def winter_wonderland_2():
        print("In the lane, snow is glistenin'")
        
    @task
    def winter_wonderland_3():
        print("A beautiful sight")
        
    @task
    def winter_wonderland_4():
        print("Oh, we're happy tonight")
        
    @task
    def your_song_for_today():
        print("Today's song is Winter Wonderland by Dean Martin!")
        print("Listen here: https://www.youtube.com/watch?v=9UeGgZVQXhc")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _ww_1 = winter_wonderland_1()
    _ww_2 = winter_wonderland_2()
    _ww_3 = winter_wonderland_3()
    _ww_4 = winter_wonderland_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _ww_1, _ww_2, _ww_3, _ww_4, _your_song_for_today, _opening_the_window)




day_1()
