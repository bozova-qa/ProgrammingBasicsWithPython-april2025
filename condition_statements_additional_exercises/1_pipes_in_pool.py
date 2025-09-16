volume_pool = int(input())
pipe_one_debit = int(input())
pipe_two_debit = int(input())
hours_absence = float(input())

pipe_one = pipe_one_debit * hours_absence
pipe_two = pipe_two_debit * hours_absence
volume_after_hours = pipe_one + pipe_two

if volume_after_hours <= volume_pool:
    print(f"The pool is {(volume_after_hours / volume_pool) * 100:.2f}% full. "
          f"Pipe 1: {(pipe_one / volume_after_hours) * 100:.2f}%. Pipe 2: {(pipe_two / volume_after_hours) * 100:.2f}%.")
elif volume_after_hours > volume_pool:
    print(f"For {hours_absence} hours the pool overflows with {volume_after_hours - volume_pool} liters.")
