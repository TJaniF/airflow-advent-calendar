from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 15th")
def day_15():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-15":
            print("It is December 15th! Let me open the window!")
        elif today > "2025-12-15":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def snowfall_1():
        print("Snowfall, snowfall")
        
    @task
    def snowfall_2():
        print("Glistening snowfall")
        
    @task
    def snowfall_3():   
        print("Snowflakes falling")
        
    @task
    def snowfall_4():
        print("Winter calling")
        
    @task
    def your_song_for_today():
        print("Today's song is Snowfall by Doris Day!")
        print("Listen here: https://www.youtube.com/watch?v=GTorIBxnKA4")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _sf_1 = snowfall_1()
    _sf_2 = snowfall_2()
    _sf_3 = snowfall_3()
    _sf_4 = snowfall_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _sf_1, _sf_2, _sf_3, _sf_4, _your_song_for_today, _opening_the_window)


day_15()
