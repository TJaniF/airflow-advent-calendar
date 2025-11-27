from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 21st")
def day_21():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-21":
            print("It is December 21st! Let me open the window!")
        elif today > "2025-12-21":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def cool_yule_1():
        print("From Coney Island to the Sunset Strip")
        
    @task
    def cool_yule_2():
        print("Somebody's gonna make a happy trip")
        
    @task
    def cool_yule_3():
        print("Tonight")
        
    @task
    def cool_yule_4():
        print("While the moon is bright")
        
    @task
    def your_song_for_today():
        print("Today's song is Cool Yule by Louis Armstrong!")
        print("Listen here: https://www.youtube.com/watch?v=F12a21dx144")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _cy_1 = cool_yule_1()
    _cy_2 = cool_yule_2()
    _cy_3 = cool_yule_3()
    _cy_4 = cool_yule_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _cy_1, _cy_2, _cy_3, _cy_4, _your_song_for_today, _opening_the_window)


day_21()
