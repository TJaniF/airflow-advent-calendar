from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 13th")
def day_13():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-13":
            print("It is December 13th! Let me open the window!")
        elif today > "2025-12-13":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def jingle_bells_1():
        print("I love those J-I-N-G-L-E bells, oh")
        
    @task
    def jingle_bells_2():
        print("Those holiday J-I-N-G-L-E bells, oh")
        
    @task
    def jingle_bells_3():
        print("Those happy J-I-N-G-L-E B-E-double-L-S")
        
    @task
    def jingle_bells_4():
        print("I love those J-I-N-G-L-E bells, oh")
        
    @task
    def your_song_for_today():
        print("Today's song is Jingle Bells by Frank Sinatra!")
        print("Listen here: https://www.youtube.com/watch?v=hLf0-lro8X8")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _jb_1 = jingle_bells_1()
    _jb_2 = jingle_bells_2()
    _jb_3 = jingle_bells_3()
    _jb_4 = jingle_bells_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _jb_1, _jb_2, _jb_3, _jb_4, _your_song_for_today, _opening_the_window)


day_13()
