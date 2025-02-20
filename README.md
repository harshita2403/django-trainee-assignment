# Django Trainee Assignment - AccuKnox  

This repository contains solutions to the **Django Signals** and **Custom Classes in Python** assignments.

---

## Topics Covered:  
### 1️ Django Signals  
- Are Django signals executed synchronously or asynchronously?  
- Do Django signals run in the same thread as the caller?  
- Do Django signals run in the same database transaction as the caller?  

### 2️ Custom Classes in Python  
- Implementation of a `Rectangle` class that supports iteration.  

---

# **Assignment 1: Django Signals**  

Django **signals** allow different parts of an application to communicate without tightly coupling them. By default, signals run **synchronously, in the same thread, and in the same database transaction** as the caller.

---

## **Question 1: Are Django Signals Executed Synchronously or Asynchronously?**  

### **Answer:**  
Django signals are executed **synchronously by default**, meaning they run **immediately** within the same execution flow as the sender.  

### **Explanation:**  
- When a signal is triggered, it is processed in the same execution context as the function that triggered it.  
- This means that the main process must wait for the signal handler to complete before continuing execution.  
- A delay in the signal handler will also delay the main function.  

**Conclusion:** Django signals are **synchronous by default**, unless explicitly configured to run asynchronously.

---

## **Question 2: Do Django Signals Run in the Same Thread as the Caller?**  

### **Answer:**  
Yes, Django signals run in the **same thread** as the caller **by default**.  

### **Explanation:**  
- Since signals are synchronous, they execute in the same thread as the function that triggered them.  
- If we check the current thread inside the signal handler, it will match the main thread unless we manually use threading or async features.  

**Conclusion:** Django signals execute in the **same thread** as the caller unless explicitly configured otherwise.

---

## **Question 3: Do Django Signals Run in the Same Database Transaction as the Caller?**  

### **Answer:**  
Yes, Django signals **run within the same database transaction** as the caller **by default**.  

### **Explanation:**  
- If a signal is triggered inside a database transaction and an error occurs, the entire transaction, including changes made by the signal, will be rolled back.  
- This ensures that data remains consistent and prevents partial updates in case of failures.  

**Conclusion:** Django signals run inside the same database transaction as the caller, unless explicitly handled differently.

---

# **Assignment 2: Custom Classes in Python**  

The `Rectangle` class meets the following requirements:  
Requires `length` and `width` to be initialized  
Supports iteration  
Outputs `{'length': VALUE}` and `{'width': VALUE}` when iterated  

### **Explanation:**  
- The class is designed to hold a rectangle's dimensions (`length` and `width`).  
- It is **iterable**, meaning we can loop over its instance and get values in a structured format.  
- The iteration order ensures that the `length` is retrieved first, followed by the `width`.  

