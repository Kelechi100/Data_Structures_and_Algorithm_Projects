# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:13:07 2024

@author: s22ilogkele
"""

from DoublyNode import DoublyLinkedList
new_list = DoublyLinkedList()
print("New List")
new_list.print_list()
print("-----------------------\n")
new_list.insert_at_start(10)
new_list.insert_at_start(15)


print("New_list after inserting at the beginning:")
new_list.print_list()


print("-----------------------------------------\n")

print("New_list after inserting at the end:")
new_list.insert_at_end(0)
new_list.insert_at_start(10)
new_list.print_list()
new_list.insert_at_start(20)
new_list.insert_at_start(25)
new_list.print_list()
new_list.insert_at_end(100)
new_list.insert_at_end(200)
new_list.insert_at_end(50)
new_list.print_list()

print("---------------------------------------\n")
print("Inserting item after another item:")
print("Original list")
new_list.print_list()
print("Output after inserting item")
new_list.insert_after_item(0, 20)

new_list.print_list()
print("---------------------------------------\n")

print("Output after inserting 35 after 50")
new_list.insert_after_item(50, 35)

new_list.print_list()
print("Output after inserting 65 before 50 ")
new_list.insert_before_item(50, 65)
new_list.print_list()
print("---------------------------------------\n")
print("Deleting elemnts from the start")
print("Original list")
new_list.print_list()
print("Output")
new_list.delete_at_start()
new_list.insert_at_end(0)
new_list.print_list()
new_list.delete_at_start()
new_list.insert_at_end(90)
new_list.insert_at_end(70)
new_list.print_list()
new_list.delete_at_start()
new_list.print_list()
new_list.delete_at_start()
new_list.print_list()
print("---------------------------------------\n")
print("Deleting elemnts from the end")
print("Original list")
new_list.print_list()
print("Output")
new_list.delete_at_end()
new_list.print_list()