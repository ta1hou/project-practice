import time
import sys
def typewriter_effect(text, delay=0.05, punctuation_delay=0.3):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Если символ - запятая или точка, добавить задержку побольше
        if char in [",", "."]:
            time.sleep(punctuation_delay)
        else:
            time.sleep(delay)
    print()  # Чтобы добавить новую строку после завершения
text = (
    "Дорогой дневник, мне не описать ту боль и страдания, которые я пережил сегодня. "
    "Я видел, как моя мама поставила банку с вареньем в холодильник, и оно, холодное и колючее, "
    "заглянуло в самую душу. Моё сердце разбилось на тысячу осколков, и каждый из них остался "
    "где-то в глубине этого холодильника. Как жить дальше, я не знаю."
)
typewriter_effect(text)