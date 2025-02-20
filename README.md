# django-trainee-assignment


This repository contains solutions to the **Django Signals** and **Custom Classes in Python** assignments.

## 📌 Topics Covered:
1. **Django Signals**
   - Are Django signals executed synchronously or asynchronously?
   - Do Django signals run in the same thread as the caller?
   - Do Django signals run in the same database transaction as the caller?

2. **Custom Classes in Python**
   - Implementation of a `Rectangle` class that supports iteration.

---

## 🚀 Assignment 1: Django Signals

Django signals are executed **synchronously by default**, meaning they run in the **same thread and database transaction** as the caller.

### **Example Code**
```python
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received!")
    print(f"Thread: {threading.current_thread().name}")
