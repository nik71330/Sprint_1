new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

#перенести task_005 из new_tasks в completed_tasks в одно действие 
completed_tasks.append(new_tasks.pop())

#удалить task_007 из new_tasks
new_tasks.remove('task_007')

#вывести последнюю задачу из new_tasks
print(new_tasks[-1])