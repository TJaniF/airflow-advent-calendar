from airflow.sdk import dag, task, chain


@dag(dag_display_name="December 23rd")
def day_23():
    @task
    def check_date():
        from include.helpers import get_todays_date

        today = get_todays_date()

        if today == "2025-12-23":
            print("It is December 23rd! Let me open the window!")
        elif today > "2025-12-23":
            print(f"It is {today}! Let's catch up and open the window!")
        else:
            print(f"It is {today}! Not time to open the window yet!")
            raise Exception(f"It is {today}! Not time to open the window yet!")
        return today

    _check_date = check_date()

    @task
    def jingle_bell_rock_1():
        print("Jingle bell, jingle bell, jingle bell rock")

    @task
    def jingle_bell_rock_2():
        print("Jingle bells swing and jingle bells ring")

    @task
    def jingle_bell_rock_3():
        print("Snowin' and blowin' up bushels of fun")

    @task
    def jingle_bell_rock_4():
        print("Now the jingle hop has begun")

    @task
    def your_song_for_today():
        print("Today's song is Jingle Bell Rock by Bobby Helms!")
        print("Listen here: https://www.youtube.com/watch?v=Z0ajuTaHBtM")

    @task
    def opening_the_window():
        import time

        time.sleep(10)
        print("Window opened! 🎉")

    _jbr_1 = jingle_bell_rock_1()
    _jbr_2 = jingle_bell_rock_2()
    _jbr_3 = jingle_bell_rock_3()
    _jbr_4 = jingle_bell_rock_4()
    _your_song_for_today = your_song_for_today()

    _opening_the_window = opening_the_window()

    chain(
        _check_date,
        _jbr_1,
        _jbr_2,
        _jbr_3,
        _jbr_4,
        _your_song_for_today,
        _opening_the_window,
    )


day_23()
