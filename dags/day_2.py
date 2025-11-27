from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 2nd")
def day_2():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-02":
            print("It is December 2nd! Let me open the window!")
        elif today > "2025-12-02":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def rockin_around_the_christmas_tree_1():
        print("Rockin' around the Christmas tree")
        
    @task
    def rockin_around_the_christmas_tree_2():
        print("At the Christmas party hop")
        
    @task
    def rockin_around_the_christmas_tree_3():
        print("Mistletoe hung where you can see")
        
    @task
    def rockin_around_the_christmas_tree_4():
        print("Every couple tries to stop")
        
    @task
    def your_song_for_today():
        print("Today's song is Rockin' Around the Christmas Tree by Brenda Lee!")
        print("Listen here: https://www.youtube.com/watch?v=TFsZy9t-qDc")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _ratct_1 = rockin_around_the_christmas_tree_1()
    _ratct_2 = rockin_around_the_christmas_tree_2()
    _ratct_3 = rockin_around_the_christmas_tree_3()
    _ratct_4 = rockin_around_the_christmas_tree_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _ratct_1, _ratct_2, _ratct_3, _ratct_4, _your_song_for_today, _opening_the_window)


day_2()
