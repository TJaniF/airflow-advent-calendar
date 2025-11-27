from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 17th")
def day_17():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-17":
            print("It is December 17th! Let me open the window!")
        elif today > "2025-12-17":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def most_wonderful_time_of_the_year_1():
        print("It's the most wonderful time of the year")
        
    @task
    def most_wonderful_time_of_the_year_2():
        print("With the kids jingle belling")
        
    @task
    def most_wonderful_time_of_the_year_3():
        print("And everyone telling you be of good cheer")
        
    @task
    def most_wonderful_time_of_the_year_4():
        print("It's the most wonderful time of the year")
        
    @task
    def your_song_for_today():
        print("Today's song is Most Wonderful Time of the Year by Andy Williams!")
        print("Listen here: https://www.youtube.com/watch?v=AN_R4pR1hck")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _mwtoty_1 = most_wonderful_time_of_the_year_1()
    _mwtoty_2 = most_wonderful_time_of_the_year_2()
    _mwtoty_3 = most_wonderful_time_of_the_year_3()
    _mwtoty_4 = most_wonderful_time_of_the_year_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _mwtoty_1, _mwtoty_2, _mwtoty_3, _mwtoty_4, _your_song_for_today, _opening_the_window)


day_17()
