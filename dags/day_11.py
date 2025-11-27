from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 11th")
def day_11():
    @task
    def check_date():
        from include.helpers import get_todays_date
        
        today = get_todays_date()

        if today == "2025-12-11":
            print("It is December 11th! Let me open the window!")
        elif today > "2025-12-11":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    @task
    def run_rudolph_run_1():
        print("Out of all the reindeers, you know you're the mastermind")
        
    @task
    def run_rudolph_run_2():
        print("Run, run Rudolph, Randolph, ain't too far behind")
        
    @task
    def run_rudolph_run_3():
        print("Run, run, Rudolph, Santa's gotta make it to town")
        
    @task
    def run_rudolph_run_4():
        print("Santa make him hurry, tell him he can take the freeway down")
        
    @task
    def your_song_for_today():
        print("Today's song is Run Rudolph Run by Chuck Berry!")
        print("Listen here: https://www.youtube.com/watch?v=YiadNVhaGwk")

    @task
    def opening_the_window():
        import time
        time.sleep(10)
        print("Window opened! 🎉")

    _check_date = check_date()
    _rrr_1 = run_rudolph_run_1()
    _rrr_2 = run_rudolph_run_2()
    _rrr_3 = run_rudolph_run_3()
    _rrr_4 = run_rudolph_run_4()
    _your_song_for_today = your_song_for_today()
    _opening_the_window = opening_the_window()

    chain(_check_date, _rrr_1, _rrr_2, _rrr_3, _rrr_4, _your_song_for_today, _opening_the_window)


day_11()
