from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 18th")
def day_18():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-18":
            print("It is December 18th! Let me open the window!")
        elif today > "2025-12-18":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def please_come_home_1():
        print("They're singing Deck The Halls")
        
    @task
    def please_come_home_2():
        print("But it's not like Christmas at all")
        
    @task
    def please_come_home_3():
        print("'Cause I remember when you were here")
        
    @task
    def please_come_home_4():
        print("And all the fun we had last year")
        
    @task
    def your_song_for_today():
        print("Today's song is Christmas (Baby Please Come Home) by Darlene Love!")
        print("Listen here: https://www.youtube.com/watch?v=4EvZOXEoJ84")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _pch_1 = please_come_home_1()
    _pch_2 = please_come_home_2()
    _pch_3 = please_come_home_3()
    _pch_4 = please_come_home_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _pch_1, _pch_2, _pch_3, _pch_4, _your_song_for_today, _opening_the_window)


day_18()
