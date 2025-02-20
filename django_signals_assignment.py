from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading
from django.db import transaction

# Question 1: Are Django Signals Synchronous or Asynchronous?
# -------------------------------------------------------------

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received!")
    print(f"Thread: {threading.current_thread().name}")

# Creating a user to trigger the signal
if __name__ == "__main__":
    print(f"Main Thread: {threading.current_thread().name}")
    user = User(username="test_user")
    user.save()

# Explanation: The signal executes within the same thread as `user.save()`, proving it is synchronous.

# Question 2: Do Django Signals Run in the Same Thread as the Caller?
# -------------------------------------------------------------------

@receiver(post_save, sender=User)
def check_thread(sender, instance, **kwargs):
    print(f"Signal executed in thread: {threading.current_thread().name}")

if __name__ == "__main__":
    print(f"Main thread: {threading.current_thread().name}")
    user = User(username="test_user_2")
    user.save()

# Explanation: The printed thread names will be the same, proving that signals run in the same thread.

# Question 3: Do Django Signals Run in the Same Database Transaction?
# -------------------------------------------------------------------

@receiver(post_save, sender=User)
def transaction_check(sender, instance, **kwargs):
    print(f"Signal inside transaction: {transaction.get_autocommit()}")

if __name__ == "__main__":
    with transaction.atomic():
        user = User(username="test_user_3")
        user.save()

# Explanation: If signals were executed in a different transaction, they wouldn’t be able to check the `transaction.atomic()` context.
