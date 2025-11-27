from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 12th")
def day_12():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-12":
            print("It is December 12th! Let me open the window!")
        elif today > "2025-12-12":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def marshmallow_world_1():
        print("The world is your snowball, see how it grows")
        
    @task
    def marshmallow_world_2():
        print("That's how it goes, whenever it snows")
        
    @task
    def marshmallow_world_3():
        print("The world is your snowball just for a song")
        
    @task
    def marshmallow_world_4():
        print("Get out and roll it along")
        
    @task
    def your_song_for_today():
        print("Today's song is Marshmallow World by Darlene Love!")
        print("Listen here: https://www.youtube.com/watch?v=AA35Ehv-uEc")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _mw_1 = marshmallow_world_1()
    _mw_2 = marshmallow_world_2()
    _mw_3 = marshmallow_world_3()
    _mw_4 = marshmallow_world_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _mw_1, _mw_2, _mw_3, _mw_4, _your_song_for_today, _opening_the_window)


day_12()
