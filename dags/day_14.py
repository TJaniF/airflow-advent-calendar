from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 14th")
def day_14():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-14":
            print("It is December 14th! Let me open the window!")
        elif today > "2025-12-14":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def the_christmas_song_1():
        print("Chestnuts roasting")
        
    @task
    def the_christmas_song_2():
        print("on an open fire")
        
    @task
    def the_christmas_song_3():
        print("Jack Frost nipping")
        
    @task
    def the_christmas_song_4():
        print("at your nose")
        
    @task
    def your_song_for_today():
        print("Today's song is The Christmas Song by Nat King Cole!")
        print("Listen here: https://www.youtube.com/watch?v=A8eWaR8ONvw")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _tcs_1 = the_christmas_song_1()
    _tcs_2 = the_christmas_song_2()
    _tcs_3 = the_christmas_song_3()
    _tcs_4 = the_christmas_song_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _tcs_1, _tcs_2, _tcs_3, _tcs_4, _your_song_for_today, _opening_the_window)


day_14()
