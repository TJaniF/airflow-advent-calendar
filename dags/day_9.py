from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 9th")
def day_9():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-09":
            print("It is December 9th! Let me open the window!")
        elif today > "2025-12-09":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def holly_jolly_christmas_1():
        print("Have a holly jolly Christmas")
        
    @task
    def holly_jolly_christmas_2():
        print("It's the best time of the year ")
        
    @task
    def holly_jolly_christmas_3():
        print("I don't know if there'll be snow")
        
    @task
    def holly_jolly_christmas_4():
        print("But have a cup of cheer")
        
    @task
    def your_song_for_today():
        print("Today's song is Holly Jolly Christmas by Burl Ives!")
        print("Listen here: https://www.youtube.com/watch?v=2uZnbzTG1jY")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _hjc_1 = holly_jolly_christmas_1()
    _hjc_2 = holly_jolly_christmas_2()
    _hjc_3 = holly_jolly_christmas_3()
    _hjc_4 = holly_jolly_christmas_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _hjc_1, _hjc_2, _hjc_3, _hjc_4, _your_song_for_today, _opening_the_window)


day_9()
