from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 20th")
def day_20():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-20":
            print("It is December 20th! Let me open the window!")
        elif today > "2025-12-20":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def shake_hands_with_santa_claus_1():
        print("Shake hands, shake hands, shake hands")
        
    @task
    def shake_hands_with_santa_claus_2():
        print("With Santa Claus")
        
    @task
    def shake_hands_with_santa_claus_3():
        print("If you want some candy, I'll bring you the candy")
        
    @task
    def shake_hands_with_santa_claus_4():
        print("Shake hands with Santa Claus")
        
    @task
    def your_song_for_today():
        print("Today's song is Shake Hands with Santa Claus by Louis Prima!")
        print("Listen here: https://www.youtube.com/watch?v=ifTUoRDAp5Y")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _shwsc_1 = shake_hands_with_santa_claus_1()
    _shwsc_2 = shake_hands_with_santa_claus_2()
    _shwsc_3 = shake_hands_with_santa_claus_3()
    _shwsc_4 = shake_hands_with_santa_claus_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _shwsc_1, _shwsc_2, _shwsc_3, _shwsc_4, _your_song_for_today, _opening_the_window)


day_20()
