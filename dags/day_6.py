from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 6th")
def day_6():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-06":
            print("It is December 6th! Let me open the window!")
        elif today > "2025-12-06":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def here_comes_santa_claus_1():
        print("Here comes Santa Claus")
        
    @task
    def here_comes_santa_claus_2():
        print("Here comes Santa Claus")
        
    @task
    def here_comes_santa_claus_3():
        print("Right down Santa Claus Lane")
        
    @task
    def here_comes_santa_claus_4():
        print("Vixen and Blitzen and all his reindeers pulling on the reins")
        
    @task
    def your_song_for_today():
        print("Today's song is Here Comes Santa Claus by Gene Autry!")
        print("Listen here: https://www.youtube.com/watch?v=E_hcT51Fo-8")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _hcsc_1 = here_comes_santa_claus_1()
    _hcsc_2 = here_comes_santa_claus_2()
    _hcsc_3 = here_comes_santa_claus_3()
    _hcsc_4 = here_comes_santa_claus_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _hcsc_1, _hcsc_2, _hcsc_3, _hcsc_4, _your_song_for_today, _opening_the_window)


day_6()
