from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 22nd")
def day_22():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-22":
            print("It is December 22nd! Let me open the window!")
        elif today > "2025-12-22":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def dig_that_crazy_santa_claus_1():
        print("Jingle, jangle")
        
    @task
    def dig_that_crazy_santa_claus_2():
        print("Dig that crazy Santa Claus with his red suit on")
        
    @task
    def dig_that_crazy_santa_claus_3():
        print("Dig that walk, that crazy talk, man, oh man, he's really gone")
        
    @task
    def dig_that_crazy_santa_claus_4():
        print("Dig that crazy Santa Claus with his bag of toys")
        
    @task
    def your_song_for_today():
        print("Today's song is Dig That Crazy Santa Claus by Ralph Marterie!")
        print("Listen here: https://www.youtube.com/watch?v=W9e81fkIVEM")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _dtcsc_1 = dig_that_crazy_santa_claus_1()
    _dtcsc_2 = dig_that_crazy_santa_claus_2()
    _dtcsc_3 = dig_that_crazy_santa_claus_3()
    _dtcsc_4 = dig_that_crazy_santa_claus_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _dtcsc_1, _dtcsc_2, _dtcsc_3, _dtcsc_4, _your_song_for_today, _opening_the_window)


day_22()
