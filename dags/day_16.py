from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 16th")
def day_16():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-16":
            print("It is December 16th! Let me open the window!")
        elif today > "2025-12-16":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def feliz_navidad_1():
        print("Feliz Navidad")
        
    @task
    def feliz_navidad_2():
        print("Próspero año y felicidad")
        
    @task
    def feliz_navidad_3():
        print("I wanna wish you a merry Christmas")
        
    @task
    def feliz_navidad_4():
        print("From the bottom of my heart")
        
    @task
    def your_song_for_today():
        print("Today's song is Feliz Navidad by José Feliciano!")
        print("Listen here: https://www.youtube.com/watch?v=0UVUW11FENs")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _fn_1 = feliz_navidad_1()
    _fn_2 = feliz_navidad_2()
    _fn_3 = feliz_navidad_3()
    _fn_4 = feliz_navidad_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _fn_1, _fn_2, _fn_3, _fn_4, _your_song_for_today, _opening_the_window)


day_16()
