from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 19th")
def day_19():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-19":
            print("It is December 19th! Let me open the window!")
        elif today > "2025-12-19":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def i_saw_mommy_kissing_santa_claus_1():
        print("I saw mommy kissing Santa Claus")
        
    @task
    def i_saw_mommy_kissing_santa_claus_2():
        print("Underneath the mistletoe last night")
        
    @task
    def i_saw_mommy_kissing_santa_claus_3():
        print("She didn't see me creep")
        
    @task
    def i_saw_mommy_kissing_santa_claus_4():
        print("Down the stairs to have a peep")
        
    @task
    def your_song_for_today():
        print("Today's song is I Saw Mommy Kissing Santa Claus by Jackson 5!")
        print("Listen here: https://www.youtube.com/watch?v=GPNu0H6jNJc")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _ismksc_1 = i_saw_mommy_kissing_santa_claus_1()
    _ismksc_2 = i_saw_mommy_kissing_santa_claus_2()
    _ismksc_3 = i_saw_mommy_kissing_santa_claus_3()
    _ismksc_4 = i_saw_mommy_kissing_santa_claus_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _ismksc_1, _ismksc_2, _ismksc_3, _ismksc_4, _your_song_for_today, _opening_the_window)


day_19()
