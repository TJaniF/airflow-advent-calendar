from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 7th")
def day_7():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-07":
            print("It is December 7th! Let me open the window!")
        elif today > "2025-12-07":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def frosty_the_snowman_1():
        print("Frosty the snowman was a jolly happy soul")
        
    @task
    def frosty_the_snowman_2():
        print("With a corncob pipe and a button nose")
        
    @task
    def frosty_the_snowman_3():
        print("And two eyes made out of coal")
        
    @task
    def frosty_the_snowman_4():
        print("Frosty the snowman is a fairy tale, they say")
        
    @task
    def your_song_for_today():
        print("Today's song is Frosty the Snowman by Jimmy Durante!")
        print("Listen here: https://www.youtube.com/watch?v=5slV6wwupbE")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _fts_1 = frosty_the_snowman_1()
    _fts_2 = frosty_the_snowman_2()
    _fts_3 = frosty_the_snowman_3()
    _fts_4 = frosty_the_snowman_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _fts_1, _fts_2, _fts_3, _fts_4, _your_song_for_today, _opening_the_window)


day_7()
