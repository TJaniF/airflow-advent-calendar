from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 3rd")
def day_3():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-03":
            print("It is December 3rd! Let me open the window!")
        elif today > "2025-12-03":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def rudolph_the_red_nosed_reindeer_1():
        print("Rudolph, the red-nosed reindeer had a very shiny nose")
        
    @task
    def rudolph_the_red_nosed_reindeer_2():
        print("and if you ever saw it you would even say it glows")
        
    @task
    def rudolph_the_red_nosed_reindeer_3():
        print("All of the other reindeer used to laugh and call him names")
        
    @task
    def rudolph_the_red_nosed_reindeer_4():
        print("They never let poor Rudolph play in any reindeer games")
        
    @task
    def your_song_for_today():
        print("Today's song is Rudolph the Red-Nosed Reindeer by Gene Autry!")
        print("Listen here: https://www.youtube.com/watch?v=44bL90HP0Ys")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _rtrnr_1 = rudolph_the_red_nosed_reindeer_1()
    _rtrnr_2 = rudolph_the_red_nosed_reindeer_2()
    _rtrnr_3 = rudolph_the_red_nosed_reindeer_3()
    _rtrnr_4 = rudolph_the_red_nosed_reindeer_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _rtrnr_1, _rtrnr_2, _rtrnr_3, _rtrnr_4, _your_song_for_today, _opening_the_window)


day_3()
