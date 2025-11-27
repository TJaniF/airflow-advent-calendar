from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 5th")
def day_5():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-05":
            print("It is December 5th! Let me open the window!")
        elif today > "2025-12-05":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def sleigh_ride_1():
        print("Just hear those sleigh bells jingling, ring tingle tingling too")
        
    @task
    def sleigh_ride_2():
        print("(Ring-a-ling-a ding-dong-ding!)")
        
    @task
    def sleigh_ride_3():
        print("Come on, it's lovely weather for a sleigh ride together with you")
        
    @task
    def sleigh_ride_4():
        print("(Ring-a-ling-a ding-dong-ding!)")
        
    @task
    def your_song_for_today():
        print("Today's song is Sleigh Ride by The Ronettes!")
        print("Listen here: https://www.youtube.com/watch?v=DkXIJe8CaIc")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _sr_1 = sleigh_ride_1()
    _sr_2 = sleigh_ride_2()
    _sr_3 = sleigh_ride_3()
    _sr_4 = sleigh_ride_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _sr_1, _sr_2, _sr_3, _sr_4, _your_song_for_today, _opening_the_window)


day_5()
