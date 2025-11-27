from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 4th")
def day_4():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-04":
            print("It is December 4th! Let me open the window!")
        elif today > "2025-12-04":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def let_it_snow_1():
        print("Oh, the weather outside is frightful")
        
    @task
    def let_it_snow_2():
        print("But the fire is so delightful")
        
    @task
    def let_it_snow_3():
        print("And since we've no place to go")
        
    @task
    def let_it_snow_4():
        print("Let it snow, let it snow, let it snow")
        
    @task
    def your_song_for_today():
        print("Today's song is Let It Snow by Dean Martin!")
        print("Listen here: https://www.youtube.com/watch?v=Rnil5LyK_B0")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _lis_1 = let_it_snow_1()
    _lis_2 = let_it_snow_2()
    _lis_3 = let_it_snow_3()
    _lis_4 = let_it_snow_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _lis_1, _lis_2, _lis_3, _lis_4, _your_song_for_today, _opening_the_window)


day_4()
